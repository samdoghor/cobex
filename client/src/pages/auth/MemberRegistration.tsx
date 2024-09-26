import { useFormik } from 'formik';
import { useEffect, useState } from "react";
import { useNavigate } from "react-router-dom";
import * as Yup from 'yup';
import Footer from "../../components/Footer";
import HeaderTwo from "../../components/HeaderTwo";
import Toaster from "../../components/Toaster";
import { HiBadgeCheck, HiExclamation, HiXCircle } from "react-icons/hi";
import { useMemberRegistrationMutation } from "../../hooks/useMember";
import Cookies from 'js-cookie';
import Confetti from '../../components/magicui/confetti';

const MemberRegistration = () => {

    const navigate = useNavigate();
    const [unfinishRegShowToast, setUnfinishRegShowToast] = useState(false);
    const [loginShowToast, setLoginShowToast] = useState(false);

    useEffect(() => {

        if (!Cookies.get('Cobex-ORD') && !Cookies.get('Cobex-ORRD')) {
            setUnfinishRegShowToast(true);
            setTimeout(() => {
                navigate('/auth/register');
            }, 0);
        }
        if (Cookies.get('Cobex-UD') && Cookies.get('Cobex-SDI')) {
            setLoginShowToast(true);
            setTimeout(() => {
                navigate('/dashboard');
            }, 3000);
        }
    }, [navigate]);

    const { mutate, isError, isSuccess, error, data } = useMemberRegistrationMutation();
    const [showToast, setShowToast] = useState(false);
    const [errorShowToast, errorSetShowToast] = useState(false);
    const [showConfetti, setShowConfetti] = useState(false);

    const organisation = Cookies.get('Cobex-ORD');
    const organisational_role = Cookies.get('Cobex-ORRD');

    const formik = useFormik({
        initialValues: {
            first_name: '',
            last_name: '',
            email: '',
            password: '',
            organisation: organisation,
            organisational_role: organisational_role,
        },
        validationSchema: Yup.object({
            first_name: Yup.string().required('First Name is required'),
            last_name: Yup.string().required('Last Name is required'),
            email: Yup.string().email('Invalid email address').required('Email is required'),
            password: Yup.string().required('Password is required'),

        }),
        onSubmit: values => {
            mutate(values);
        },
    });

    useEffect(() => {
        if (isSuccess) {
            setShowToast(true);
            setShowConfetti(true)
            setTimeout(() => {
                setShowToast(false);
                setShowConfetti(false);
            }, 3000);
            setTimeout(() => {
                navigate('/auth/login');
            }, 3500);
            Cookies.remove('Cobex-ORD')
            Cookies.remove('Cobex-ORRD')
        }

        if (isError) {
            errorSetShowToast(true);
            setTimeout(() => {
                errorSetShowToast(false);
            }, 3000);
        }
    }, [isSuccess, isError, data, error, navigate]);
    return (
        <>
            <HeaderTwo />
            <div className="bg-stone-950 md:min-h-screen py-20 flex justify-center items-center">
                <div className="border border-gray-200 rounded-xl shadow-sm md:w-[40%] w-96">
                    <div className="p-4 sm:p-7">
                        <div className="mt-5">
                            <div className="py-3 flex items-center text-xs text-gray-400 uppercase before:flex-1 before:border-t before:border-gray-200 before:me-6 after:flex-1 after:border-t after:border-gray-200 after:ms-6">President Data</div>

                            <form onSubmit={formik.handleSubmit}>
                                <div className="grid gap-y-4 pb-4">
                                    <div>
                                        <label htmlFor="first_name" className="block text-sm mb-2 text-gray-100">First Name</label>
                                        <div className="relative">
                                            <input type="text" id="first_name" name="first_name" className="py-3 px-4 block w-full border-gray-200 rounded-lg text-sm focus:border-blue-500 focus:ring-blue-500 disabled:opacity-50 disabled:pointer-events-none" required aria-describedby="first-name-error" placeholder="Presidents First Name" onChange={formik.handleChange} value={formik.values.first_name} />
                                            <div className="hidden absolute inset-y-0 end-0 pointer-events-none pe-3">
                                                <svg className="size-5 text-red-500" width="16" height="16" fill="currentColor" viewBox="0 0 16 16" aria-hidden="true">
                                                    <path d="M16 8A8 8 0 1 1 0 8a8 8 0 0 1 16 0zM8 4a.905.905 0 0 0-.9.995l.35 3.507a.552.552 0 0 0 1.1 0l.35-3.507A.905.905 0 0 0 8 4zm.002 6a1 1 0 1 0 0 2 1 1 0 0 0 0-2z" />
                                                </svg>
                                            </div>
                                        </div>
                                        <p className="hidden text-xs text-red-600 mt-2" id="first-name-error">Please include a valid first name so we can get back to you</p>
                                    </div>

                                    <div>
                                        <label htmlFor="last_name" className="block text-sm mb-2 text-gray-100">Last Name</label>
                                        <div className="relative">
                                            <input type="text" id="last_name" name="last_name" className="py-3 px-4 block w-full border-gray-200 rounded-lg text-sm focus:border-blue-500 focus:ring-blue-500 disabled:opacity-50 disabled:pointer-events-none" required aria-describedby="last-name-error" placeholder="Presidents Last Name" onChange={formik.handleChange} value={formik.values.last_name} />
                                            <div className="hidden absolute inset-y-0 end-0 pointer-events-none pe-3">
                                                <svg className="size-5 text-red-500" width="16" height="16" fill="currentColor" viewBox="0 0 16 16" aria-hidden="true">
                                                    <path d="M16 8A8 8 0 1 1 0 8a8 8 0 0 1 16 0zM8 4a.905.905 0 0 0-.9.995l.35 3.507a.552.552 0 0 0 1.1 0l.35-3.507A.905.905 0 0 0 8 4zm.002 6a1 1 0 1 0 0 2 1 1 0 0 0 0-2z" />
                                                </svg>
                                            </div>
                                        </div>
                                        <p className="hidden text-xs text-red-600 mt-2" id="last-name-error">Please include a valid last name so we can get back to you</p>
                                    </div>

                                    <div>
                                        <label htmlFor="email" className="block text-sm mb-2 text-gray-100">Email Address</label>
                                        <div className="relative">
                                            <input type="email" id="email" name="email" className="py-3 px-4 block w-full border-gray-200 rounded-lg text-sm focus:border-blue-500 focus:ring-blue-500 disabled:opacity-50 disabled:pointer-events-none" required aria-describedby="last-name-error" placeholder="Presidents Email Address" onChange={formik.handleChange} value={formik.values.email} />
                                            <div className="hidden absolute inset-y-0 end-0 pointer-events-none pe-3">
                                                <svg className="size-5 text-red-500" width="16" height="16" fill="currentColor" viewBox="0 0 16 16" aria-hidden="true">
                                                    <path d="M16 8A8 8 0 1 1 0 8a8 8 0 0 1 16 0zM8 4a.905.905 0 0 0-.9.995l.35 3.507a.552.552 0 0 0 1.1 0l.35-3.507A.905.905 0 0 0 8 4zm.002 6a1 1 0 1 0 0 2 1 1 0 0 0 0-2z" />
                                                </svg>
                                            </div>
                                        </div>
                                        <p className="hidden text-xs text-red-600 mt-2" id="last-name-error">Please include a valid email so we can get back to you</p>
                                    </div>

                                    <div>
                                        <label htmlFor="password" className="block text-sm mb-2 text-gray-100">Password</label>
                                        <div className="relative">
                                            <input type="password" id="password" name="password" className="py-3 px-4 block w-full border-gray-200 rounded-lg text-sm focus:border-blue-500 focus:ring-blue-500 disabled:opacity-50 disabled:pointer-events-none" required aria-describedby="last-name-error" placeholder="Enter Password" onChange={formik.handleChange} value={formik.values.password} />
                                            <div className="hidden absolute inset-y-0 end-0 pointer-events-none pe-3">
                                                <svg className="size-5 text-red-500" width="16" height="16" fill="currentColor" viewBox="0 0 16 16" aria-hidden="true">
                                                    <path d="M16 8A8 8 0 1 1 0 8a8 8 0 0 1 16 0zM8 4a.905.905 0 0 0-.9.995l.35 3.507a.552.552 0 0 0 1.1 0l.35-3.507A.905.905 0 0 0 8 4zm.002 6a1 1 0 1 0 0 2 1 1 0 0 0 0-2z" />
                                                </svg>
                                            </div>
                                        </div>
                                        <p className="hidden text-xs text-red-600 mt-2" id="last-name-error">Please include a valid password so we can get back to you</p>
                                    </div>

                                    <button type="submit" className="w-full py-3 px-4 inline-flex justify-center items-center gap-x-2 text-sm font-medium rounded-lg border border-transparent bg-themeThree text-white hover:bg-themeTwo focus:outline-none focus:bg-themeTwo disabled:opacity-50 disabled:pointer-events-none">Create Account</button>
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
                    codeStatus="You have no previous registeration process, redirecting..."
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
            {showConfetti && (
                <div className="w-full h-screen absolute inset-0 flex justify-center items-center pointer-events-none">
                    <Confetti />
                </div>
            )}
            <Footer />
        </>
    )
}

export default MemberRegistration