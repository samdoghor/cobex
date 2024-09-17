
const Header = () => {
    return (
        <>
            <header className="bg-neutral-900">
                <div className="mx-auto max-w-screen-xl px-4 sm:px-6 lg:px-8">
                    <div className="flex h-16 items-center justify-between">
                        <div className="md:flex md:items-center md:gap-12">
                            <a className="block text-teal-600 dark:text-teal-600" href="#">
                                <span className="sr-only">Home</span>
                                <img src="/assets/images/cobex-logo-full-white.svg" alt="Cobex" width={150} />
                            </a>
                        </div>

                        <div className="hidden md:block">
                            <nav aria-label="Global">
                                <ul className="flex items-center gap-6 text-sm">
                                    <li>
                                        <a
                                            className="text-gray-200 transition hover:text-gray-500/75"
                                            href="#"
                                        >
                                            Cooperatives
                                        </a>
                                    </li>

                                    <li>
                                        <a
                                            className="text-gray-200 transition hover:text-gray-500/75"
                                            href="#"
                                        >
                                            How it works
                                        </a>
                                    </li>

                                    <li>
                                        <a
                                            className="text-gray-200 transition hover:text-gray-500/75"
                                            href="#"
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
                                        <a
                                            className="text-gray-200 transition hover:text-gray-500/75"
                                            href="#"
                                        >
                                            Support
                                        </a>
                                    </li>
                                </ul>
                            </nav>
                        </div>

                        <div className="flex items-center gap-4">
                            <div className="sm:flex sm:gap-4">
                                <a
                                    className="rounded-md bg-themeThree px-5 py-2.5 text-sm font-medium text-white shadow"
                                    href="#"
                                >
                                    Login
                                </a>

                                <div className="hidden sm:flex">
                                    <a
                                        className="rounded-md bg-gray-100 px-5 py-2.5 text-sm font-medium text-themeThree"
                                        href="#"
                                    >
                                        Register
                                    </a>
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
                                        stroke-width="2"
                                    >
                                        <path stroke-linecap="round" stroke-linejoin="round" d="M4 6h16M4 12h16M4 18h16" />
                                    </svg>
                                </button>
                            </div>
                        </div>
                    </div>
                </div>
            </header>
        </>
    )
}

export default Header