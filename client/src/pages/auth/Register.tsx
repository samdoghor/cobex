import { useFormik } from 'formik';
import { useEffect, useState } from "react";
import { Link, useNavigate } from "react-router-dom";
import * as Yup from 'yup';
import Footer from "../../components/Footer";
import Header from "../../components/Header";
import Toaster from "../../components/Toaster";
import { HiBadgeCheck, HiExclamation, HiXCircle } from "react-icons/hi";
import Cookies from 'js-cookie';
import { useOrganisationRegistrationMutation } from '../../hooks/useOrganisation';
import { useOrganisationRoleRegistrationMutation } from '../../hooks/useOrganisationRole';


const Register = () => {
    const navigate = useNavigate();
    const [unfinishRegShowToast, setUnfinishRegShowToast] = useState(false);
    const [loginShowToast, setLoginShowToast] = useState(false);

    useEffect(() => {

        if (Cookies.get('Cobex-ORD') && Cookies.get('Cobex-ORRD')) {
            setUnfinishRegShowToast(true);
            setTimeout(() => {
                navigate('/auth/register/member');
            }, 3000);
        }
        if (Cookies.get('Cobex-UD') && Cookies.get('Cobex-SDI')) {
            setLoginShowToast(true);
            setTimeout(() => {
                navigate('/dashboard');
            }, 3000);
        }
    }, [navigate]);

    const { mutate, isError, isSuccess, error, data } = useOrganisationRegistrationMutation();
    const { mutate: registerRole, isSuccess: isRoleSuccess, data: roleData } = useOrganisationRoleRegistrationMutation();
    const [showToast, setShowToast] = useState(false);
    const [errorShowToast, errorSetShowToast] = useState(false);
    const [roleRegistered, setRoleRegistered] = useState(false);

    const formik = useFormik({
        initialValues: {
            full_name: '',
            email: '',
        },
        validationSchema: Yup.object({
            full_name: Yup.string().required('Full Name is required'),
            email: Yup.string().email('Invalid email address').required('Email is required'),
        }),
        onSubmit: values => {
            mutate(values);
        },
    });

    useEffect(() => {
        if (isSuccess && !roleRegistered) {
            registerRole({
                role: "president",
                is_top_role: true,
                is_member_role: false,
                role_position: 7,
                organisation: data?.data?.id
            });

            setShowToast(true);
            setTimeout(() => {
                setShowToast(false);
            }, 3000);

            Cookies.set('Cobex-ORD', data?.data?.id, {
                expires: 7,
                secure: true,
                sameSite: 'strict',
                path: '/',
            });

            setRoleRegistered(true);
        }

        if (isRoleSuccess && roleData?.data?.id) {
            Cookies.set('Cobex-ORRD', roleData?.data?.id, {
                expires: 1,
                secure: true,
                sameSite: 'strict',
                path: '/',
            });

            setTimeout(() => {
                navigate('/auth/register/member');
            }, 3500);
        }

        if (isError) {
            errorSetShowToast(true);
            setTimeout(() => {
                errorSetShowToast(false);
            }, 3000);
        }
    }, [isSuccess, isError, data, error, navigate, registerRole, roleData, isRoleSuccess, roleRegistered]);
    return (
        <>
            <Header />
            <div className="bg-stone-950 min-h-screen py-20 flex justify-center items-center">
                <div className="border border-gray-200 rounded-xl shadow-sm w-[40%]">
                    <div className="p-4 sm:p-7">
                        <div className="text-center">
                            <h1 className="block text-2xl font-bold text-gray-400">Sign up</h1>
                            <p className="mt-2 text-sm text-gray-100">
                                Already have an account?
                                <Link className="text-gray-100 decoration-2 hover:underline focus:outline-none focus:underline font-medium ps-2" to="/auth/login"> Sign in here </Link>
                            </p>
                        </div>

                        <div className="text-center">
                            <p className="mt-4 text-normal font-semibold text-gray-100">
                                Only the organization president needs to create an account. The president will send a registration link to other members to join.
                            </p>
                        </div>

                        <div className="mt-5">
                            <div className="py-3 flex items-center text-xs text-gray-400 uppercase before:flex-1 before:border-t before:border-gray-200 before:me-6 after:flex-1 after:border-t after:border-gray-200 after:ms-6">Organisation Data</div>

                            <form onSubmit={formik.handleSubmit}>
                                <div className="grid gap-y-4 pb-4">
                                    <div>
                                        <label htmlFor="full_name" className="block text-sm mb-2 text-gray-100">Organisation Full Name</label>
                                        <div className="relative">
                                            <input type="text" id="full_name" name="full_name" className="py-3 px-4 block w-full border-gray-200 rounded-lg text-sm focus:border-blue-500 focus:ring-blue-500 disabled:opacity-50 disabled:pointer-events-none" required aria-describedby="email-error" placeholder="Organisation's Full Name" onChange={formik.handleChange} value={formik.values.full_name} />
                                            <div className="hidden absolute inset-y-0 end-0 pointer-events-none pe-3">
                                                <svg className="size-5 text-red-500" width="16" height="16" fill="currentColor" viewBox="0 0 16 16" aria-hidden="true">
                                                    <path d="M16 8A8 8 0 1 1 0 8a8 8 0 0 1 16 0zM8 4a.905.905 0 0 0-.9.995l.35 3.507a.552.552 0 0 0 1.1 0l.35-3.507A.905.905 0 0 0 8 4zm.002 6a1 1 0 1 0 0 2 1 1 0 0 0 0-2z" />
                                                </svg>
                                            </div>
                                        </div>
                                        <p className="hidden text-xs text-red-600 mt-2" id="email-error">Please include a valid email address so we can get back to you</p>
                                    </div>

                                    <div>
                                        <label htmlFor="email" className="block text-sm mb-2 text-gray-100">Organisation Email address</label>
                                        <div className="relative">
                                            <input type="email" id="email" name="email" className="py-3 px-4 block w-full border-gray-200 rounded-lg text-sm focus:border-blue-500 focus:ring-blue-500 disabled:opacity-50 disabled:pointer-events-none" required aria-describedby="email-error" placeholder="Organisation's Email Address" onChange={formik.handleChange} value={formik.values.email} />
                                            <div className="hidden absolute inset-y-0 end-0 pointer-events-none pe-3">
                                                <svg className="size-5 text-red-500" width="16" height="16" fill="currentColor" viewBox="0 0 16 16" aria-hidden="true">
                                                    <path d="M16 8A8 8 0 1 1 0 8a8 8 0 0 1 16 0zM8 4a.905.905 0 0 0-.9.995l.35 3.507a.552.552 0 0 0 1.1 0l.35-3.507A.905.905 0 0 0 8 4zm.002 6a1 1 0 1 0 0 2 1 1 0 0 0 0-2z" />
                                                </svg>
                                            </div>
                                        </div>
                                        <p className="hidden text-xs text-red-600 mt-2" id="email-error">Please include a valid email address so we can get back to you</p>
                                    </div>

                                    <button type="submit" className="w-full py-3 px-4 inline-flex justify-center items-center gap-x-2 text-sm font-medium rounded-lg border border-transparent bg-themeThree text-white hover:bg-themeTwo focus:outline-none focus:bg-themeTwo disabled:opacity-50 disabled:pointer-events-none">
                                        Next
                                    </button>
                                </div>
                            </form>
                        </div>
                    </div>
                </div>
            </div>
            {showToast && (
                <Toaster
                    codeStatus={data?.code_status}
                    onDismiss={() => setShowToast(false)}
                    bgColor="bg-green-950"
                    toastIcon={<HiBadgeCheck className="h-5 w-5 bg-green-700 rounded-lg" />}
                />
            )}
            {errorShowToast && (
                <Toaster
                    //@ts-expect-error - datatype error
                    codeStatus={error?.response?.data?.code_message}
                    onDismiss={() => errorSetShowToast(false)}
                    bgColor="bg-red-950"
                    toastIcon={<HiXCircle className="h-5 w-5 bg-red-700 rounded-lg" />}
                />
            )}
            {unfinishRegShowToast && (
                <Toaster
                    codeStatus="You have an unfinished registeration process, redirecting..."
                    onDismiss={() => setUnfinishRegShowToast(false)}
                    bgColor="bg-yellow-950"
                    toastIcon={<HiExclamation className="h-5 w-5 bg-yellow-700 rounded-lg" />}
                />
            )}
            {loginShowToast && (
                <Toaster
                    codeStatus="You are logged in, redirecting..."
                    onDismiss={() => setLoginShowToast(false)}
                    bgColor="bg-yellow-950"
                    toastIcon={<HiExclamation className="h-5 w-5 bg-yellow-700 rounded-lg" />}
                />
            )}
            <Footer />
        </>
    )
}

export default Register