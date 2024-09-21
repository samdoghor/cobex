import { Link, useNavigate } from "react-router-dom";
import { useEffect, useState } from "react";
import Cookies from 'js-cookie';
import { HiExclamation } from "react-icons/hi";
import Toaster from "./Toaster";

const Header = () => {
    const navigate = useNavigate();
    const [errorlogoutShowToast, setErrorLogoutShowToast] = useState(false);
    const [unfinishRegShowToast, setUnfinishRegShowToast] = useState(false);

    useEffect(() => {

        if (Cookies.get('Cobex-ORD') && Cookies.get('Cobex-ORRD')) {
            setUnfinishRegShowToast(true);
            setTimeout(() => {
                navigate('/auth/register/member');
            }, 3000);
        }
        if (Cookies.get('Cobex-UD') && Cookies.get('Cobex-SDI')) {
            setErrorLogoutShowToast(true);
            setTimeout(() => {
                navigate('/dashboard');
            }, 3000);
        }
    }, [navigate]);

    return (
        <>
            <header className="bg-neutral-900">
                <div className="mx-auto max-w-screen-xl px-4 sm:px-6 lg:px-8">
                    <div className="flex h-16 items-center justify-between">
                        <div className="md:flex md:items-center md:gap-12">
                            <Link className="block text-teal-600 dark:text-teal-600" to="/">
                                <span className="sr-only">Home</span>
                                <img src="/assets/images/cobex-logo-full-white.svg" alt="Cobex" width={150} />
                            </Link>
                        </div>

                        <div className="hidden md:block">
                            <nav aria-label="Global">
                                <ul className="flex items-center gap-6 text-sm">
                                    <li>
                                        <Link className="text-gray-200 transition hover:text-gray-500/75" to="/cooperatives"> Cooperatives </Link>
                                    </li>

                                    <li>
                                        <Link className="text-gray-200 transition hover:text-gray-500/75" to="/learn"> Learn </Link>
                                    </li>

                                    <li>
                                        <a
                                            className="text-gray-200 transition hover:text-gray-500/75"
                                            href="#faq"
                                        >
                                            FAQ
                                        </a>
                                    </li>

                                    <li>
                                        <a
                                            className="text-gray-200 transition hover:text-gray-500/75"
                                            href="#"
                                        >
                                            Integration
                                        </a>
                                    </li>

                                    <li>
                                        <Link className="text-gray-200 transition hover:text-gray-500/75" to="/contact"> Support </Link>
                                    </li>
                                </ul>
                            </nav>
                        </div>

                        <div className="flex items-center gap-4">
                            <div className="sm:flex sm:gap-4">
                                <Link className="rounded-md bg-themeThree px-5 py-2.5 text-sm font-medium text-white shadow" to="/auth/login"> Login </Link>

                                <div className="hidden sm:flex">
                                    <Link className="rounded-md bg-gray-100 px-5 py-2.5 text-sm font-medium text-themeThree" to="/auth/register"> Register </Link>
                                </div>
                            </div>

                            <div className="block md:hidden">
                                <button
                                    className="rounded bg-gray-100 p-2 text-gray-600 transition hover:text-gray-600/75 dark:bg-gray-800"
                                >
                                    <svg
                                        xmlns="http://www.w3.org/2000/svg"
                                        className="size-5"
                                        fill="none"
                                        viewBox="0 0 24 24"
                                        stroke="currentColor"
                                        strokeWidth="2"
                                    >
                                        <path strokeLinecap="round" strokeLinejoin="round" d="M4 6h16M4 12h16M4 18h16" />
                                    </svg>
                                </button>
                            </div>
                        </div>
                    </div>
                </div>
            </header>
            {unfinishRegShowToast && (
                <Toaster
                    codeStatus="You have an unfinished registeration process, redirecting..."
                    onDismiss={() => setUnfinishRegShowToast(false)}
                    bgColor="bg-yellow-950"
                    toastIcon={<HiExclamation className="h-5 w-5 bg-yellow-700 rounded-lg" />}
                />
            )}
            {errorlogoutShowToast && (
                <Toaster
                    codeStatus="You are logged in, redirecting..."
                    onDismiss={() => setErrorLogoutShowToast(false)}
                    bgColor="bg-yellow-950"
                    toastIcon={<HiExclamation className="h-5 w-5 bg-yellow-700 rounded-lg" />}
                />
            )}
        </>
    )
}

export default Header