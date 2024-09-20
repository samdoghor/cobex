import { useFormik } from 'formik';
import { useEffect, useState } from "react";
import { Link, useNavigate } from "react-router-dom";
import * as Yup from 'yup';
import Footer from "../../components/Footer";
import Header from "../../components/Header";
import Toaster from "../../components/Toaster";
import { useMemberLoginMutation } from "../../hooks/useMember";
import { HiCheck, HiX } from "react-icons/hi";
import Cookies from 'js-cookie';

const Login = () => {
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

    const { mutate, isError, isSuccess, error, data } = useMemberLoginMutation();
    const [showToast, setShowToast] = useState(false);
    const [errorShowToast, errorSetShowToast] = useState(false);

    const formik = useFormik({
        initialValues: {
            email: '',
            password: '',
        },
        validationSchema: Yup.object({
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
            setTimeout(() => {
                setShowToast(false);
            }, 3000);
            setTimeout(() => {
                navigate('/dashboard');
            }, 3500);
            Cookies.set('Cobex-UD', data?.data?.access_token, {
                // HttpOnly: true,
                expires: 7,
                secure: true,
                sameSite: 'strict',
                path: '/',
            });
            Cookies.set('Cobex-SDI', data?.data?.session_id, {
                // HttpOnly: true,
                expires: 7,
                secure: true,
                sameSite: 'strict',
                path: '/',
            });
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
            <Header />
            <div className="bg-stone-950 min-h-screen py-20 flex justify-center items-center">
                <div className="border border-gray-200 rounded-xl shadow-sm w-[40%]">
                    <div className="p-4 sm:p-7">
                        <div className="text-center">
                            <h1 className="block text-2xl font-bold text-gray-400">Sign in</h1>
                            <p className="mt-2 text-sm text-gray-100">
                                Don't have an account yet?
                                <Link className="text-gray-100 decoration-2 hover:underline focus:outline-none focus:underline font-medium ps-2" to="/auth/register"> Sign up here </Link>
                            </p>
                        </div>

                        <div className="mt-5">
                            <form onSubmit={formik.handleSubmit}>
                                <div className="grid gap-y-4">
                                    <div>
                                        <label htmlFor="email" className="block text-sm mb-2 text-gray-100">Email address</label>
                                        <div className="relative">
                                            <input type="email" id="email" name="email" className="py-3 px-4 block w-full border-gray-200 rounded-lg text-sm focus:border-blue-500 focus:ring-blue-500 disabled:opacity-50 disabled:pointer-events-none" required aria-describedby="email-error" onChange={formik.handleChange}
                                                value={formik.values.email} placeholder="Enter Email Address"
                                            />
                                            <div className="hidden absolute inset-y-0 end-0 pointer-events-none pe-3">
                                                <svg className="size-5 text-red-500" width="16" height="16" fill="currentColor" viewBox="0 0 16 16" aria-hidden="true">
                                                    <path d="M16 8A8 8 0 1 1 0 8a8 8 0 0 1 16 0zM8 4a.905.905 0 0 0-.9.995l.35 3.507a.552.552 0 0 0 1.1 0l.35-3.507A.905.905 0 0 0 8 4zm.002 6a1 1 0 1 0 0 2 1 1 0 0 0 0-2z" />
                                                </svg>
                                            </div>
                                        </div>
                                        <p className="hidden text-xs text-red-600 mt-2" id="email-error">Please include a valid email address so we can get back to you</p>
                                    </div>

                                    <div>
                                        <div className="flex justify-between items-center">
                                            <label htmlFor="password" className="block text-sm mb-2 text-gray-100">Password</label>
                                            <a className="inline-flex items-center gap-x-1 text-sm text-themeThree decoration-2 hover:underline focus:outline-none focus:underline font-medium" href="../examples/html/recover-account.html">Forgot password?</a>
                                        </div>
                                        <div className="relative">
                                            <input type="password" id="password" name="password" className="py-3 px-4 block w-full border-gray-200 rounded-lg text-sm focus:border-blue-500 focus:ring-blue-500 disabled:opacity-50 disabled:pointer-events-none" required aria-describedby="password-error" onChange={formik.handleChange} value={formik.values.password} placeholder="Enter Password" />
                                            <div className="hidden absolute inset-y-0 end-0 pointer-events-none pe-3">
                                                <svg className="size-5 text-red-500" width="16" height="16" fill="currentColor" viewBox="0 0 16 16" aria-hidden="true">
                                                    <path d="M16 8A8 8 0 1 1 0 8a8 8 0 0 1 16 0zM8 4a.905.905 0 0 0-.9.995l.35 3.507a.552.552 0 0 0 1.1 0l.35-3.507A.905.905 0 0 0 8 4zm.002 6a1 1 0 1 0 0 2 1 1 0 0 0 0-2z" />
                                                </svg>
                                            </div>
                                        </div>
                                        <p className="hidden text-xs text-red-600 mt-2" id="password-error">8+ characters required</p>
                                    </div>

                                    <div className="flex items-center">
                                        <div className="flex">
                                            <input id="remember-me" name="remember-me" type="checkbox" className="shrink-0 mt-0.5 border-gray-200 rounded text-themeThree focus:ring-themeThree" />
                                        </div>
                                        <div className="ms-3">
                                            <label htmlFor="remember-me" className="text-sm text-gray-100">Remember me</label>
                                        </div>
                                    </div>

                                    <button type="submit" className="w-full py-3 px-4 inline-flex justify-center items-center gap-x-2 text-sm font-medium rounded-lg border border-transparent bg-themeThree hover:bg-themeTwo text-white hover:themeTwo focus:outline-none focus:themeTwo disabled:opacity-50 disabled:pointer-events-none">Sign in</button>
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
                    toastIcon={<HiCheck className="h-5 w-5 bg-green-700 rounded-lg" />}
                />
            )}
            {errorShowToast && (
                <Toaster
                    //@ts-expect-error - datatype error
                    codeStatus={error?.response?.data?.code_message}
                    onDismiss={() => errorSetShowToast(false)}
                    bgColor="bg-red-950"
                    toastIcon={<HiX className="h-5 w-5 bg-red-700 rounded-lg" />}
                />
            )}
            {unfinishRegShowToast && (
                <Toaster
                    codeStatus="You have an unfinished registeration process, redirecting..."
                    onDismiss={() => setUnfinishRegShowToast(false)}
                    bgColor="bg-yellow-950"
                    toastIcon={<HiX className="h-5 w-5 bg-yellow-700 rounded-lg" />}
                />
            )}
            {loginShowToast && (
                <Toaster
                    codeStatus="You are logged in, redirecting..."
                    onDismiss={() => setLoginShowToast(false)}
                    bgColor="bg-yellow-950"
                    toastIcon={<HiX className="h-5 w-5 bg-yellow-700 rounded-lg" />}
                />
            )}
            <Footer />
        </>
    )
}

export default Login