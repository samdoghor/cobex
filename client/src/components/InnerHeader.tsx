import { CircleUser, Menu, Search } from "lucide-react"
import { DropdownMenu, DropdownMenuContent, DropdownMenuItem, DropdownMenuLabel, DropdownMenuTrigger } from "./ui/dropdown-menu"
import { Button } from "@/components/ui/button"
import { useEffect, useState } from "react";
import { useMemberLogoutMutation } from "@/hooks/useMember";
import { Link, useNavigate } from "react-router-dom";
import Cookies from 'js-cookie';
import { HiBadgeCheck, HiExclamation, HiXCircle } from "react-icons/hi";
import Toaster from "./Toaster";
import { Sheet, SheetContent, SheetTrigger } from "./ui/sheet";
import { Input } from "./ui/input";


const InnerHeader = () => {
    const navigate = useNavigate();
    const [logoutShowToast, setLogoutShowToast] = useState(false);
    const [errorlogoutShowToast, setErrorLogoutShowToast] = useState(false);
    const [errorShowToast, errorSetShowToast] = useState(false);
    const [unfinishRegShowToast, setUnfinishRegShowToast] = useState(false);
    const { mutate, isError, isSuccess, data, error } = useMemberLogoutMutation();

    useEffect(() => {

        if (Cookies.get('Cobex-ORD') && Cookies.get('Cobex-ORRD')) {
            setUnfinishRegShowToast(true);
            setTimeout(() => {
                navigate('/auth/register/member');
            }, 3000);
        }
        if (!Cookies.get('Cobex-UD') && !Cookies.get('Cobex-SDI')) {
            setErrorLogoutShowToast(true);
            setTimeout(() => {
                navigate('/auth/login');
            }, 3000);
        }
    }, [navigate]);

    useEffect(() => {
        if (isSuccess) {
            setLogoutShowToast(true);
            setTimeout(() => {
                setLogoutShowToast(false);
            }, 3000);
            setTimeout(() => {
                navigate('/');
            }, 3500);
            Cookies.remove('Cobex-SDI')
            Cookies.remove('Cobex-UD')
            localStorage.removeItem('Cobex-EUI');
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
            <header className="bg-neutral-950 sticky top-0 flex h-16 items-center gap-4 border-b bg-background px-4 md:px-6 z-50">
                <nav className="hidden flex-col gap-6 text-lg font-medium md:flex md:flex-row md:items-center md:gap-5 md:text-sm lg:gap-6">
                    <div className="md:flex md:items-center">
                        <Link className="block text-teal-600 dark:text-teal-600" to="/dashboard">
                            <span className="sr-only">Home</span>
                            <img src="/assets/images/cobex-logo-full-white.svg" alt="Cobex" className="object-fill h-96" />
                        </Link>
                    </div>
                    <Link
                        to="/dashboard"
                        className="text-white hover:text-gray-300"
                    >
                        Dashboard
                    </Link>
                    <Link
                        to="/overview"
                        className="text-white hover:text-gray-300"
                    >
                        Organisation
                    </Link>
                    <Link
                        to="/events"
                        className="text-white hover:text-gray-300"
                    >
                        Events
                    </Link>
                    <Link
                        to="/levies"
                        className="text-white hover:text-gray-300"
                    >
                        Levies
                    </Link>
                    <Link
                        to="#"
                        className="text-white hover:text-gray-300"
                    >
                        Transations
                    </Link>
                </nav>
                <Sheet>
                    <SheetTrigger asChild>
                        <Button
                            variant="outline"
                            size="icon"
                            className="shrink-0 md:hidden"
                        >
                            <Menu className="h-5 w-5" />
                            <span className="sr-only">Toggle navigation menu</span>
                        </Button>
                    </SheetTrigger>
                    <SheetContent side="left">
                        <nav className="grid gap-6 text-lg font-medium">
                            <div className="md:flex md:items-center md:gap-12">
                                <Link className="block text-teal-600 dark:text-teal-600" to="/">
                                    <span className="sr-only">Home</span>
                                    <img src="/assets/images/cobex-logo-full-white.svg" alt="Cobex" width={400} />
                                </Link>
                            </div>
                            <Link
                                to="/dashboard"
                                className="text-white hover:text-gray-300"
                            >
                                Dashboard
                            </Link>
                            <Link
                                to="/overview"
                                className="text-white hover:text-gray-300"
                            >
                                Organisation
                            </Link>
                            <Link
                                to="/events"
                                className="text-white hover:text-gray-300"
                            >
                                Events
                            </Link>
                            <Link
                                to="/levies"
                                className="text-white hover:text-gray-300"
                            >
                                Levies
                            </Link>
                            <Link
                                to="#"
                                className="text-white hover:text-gray-300"
                            >
                                Transations
                            </Link>
                        </nav>
                    </SheetContent>
                </Sheet>
                <div className="flex w-full items-center gap-4 md:ml-auto md:gap-2 lg:gap-4">
                    <form className="ml-auto flex-1 sm:flex-initial">
                        <div className="relative">
                            <Search className="absolute left-2.5 top-2.5 h-4 w-4 text-muted-foreground" />
                            <Input
                                type="search"
                                placeholder="Search products..."
                                className="pl-8 sm:w-[300px] md:w-[200px] lg:w-[300px]"
                            />
                        </div>
                    </form>
                    <DropdownMenu>
                        <DropdownMenuTrigger asChild>
                            <Button variant="secondary" size="icon" className="rounded-full">
                                <CircleUser className="h-5 w-5" />
                                <span className="sr-only">Toggle user menu</span>
                            </Button>
                        </DropdownMenuTrigger>
                        <DropdownMenuContent align="end" className="bg-neutral-950 text-white hover:cursor-pointer">
                            <DropdownMenuLabel>Account Details</DropdownMenuLabel>
                            <Link to="/dashboard/settings/biodata"><DropdownMenuItem className="bg-neutral-950 text-white hover:cursor-pointer">Settings</DropdownMenuItem></Link>
                            <DropdownMenuItem className="bg-neutral-950 text-white hover:cursor-pointer">Support</DropdownMenuItem>
                            <DropdownMenuItem className="bg-neutral-950 text-white hover:cursor-pointer" onClick={() => mutate()}>Logout</DropdownMenuItem>
                        </DropdownMenuContent>
                    </DropdownMenu>
                </div>
            </header>


            {logoutShowToast && (
                <Toaster
                    codeStatus={data?.code_status}
                    onDismiss={() => setLogoutShowToast(false)}
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
            {errorlogoutShowToast && (
                <Toaster
                    codeStatus="You are not logged in, redirecting..."
                    onDismiss={() => setErrorLogoutShowToast(false)}
                    bgColor="bg-yellow-950"
                    toastIcon={<HiExclamation className="h-5 w-5 bg-yellow-700 rounded-lg" />}
                />
            )}
        </>
    )
}

export default InnerHeader