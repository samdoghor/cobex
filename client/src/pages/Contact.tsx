import { Link } from "react-router-dom"
import Footer from "../components/Footer"
import Header from "../components/Header"

const Contact = () => {
    return (
        <>
            <Header />
            <section className="overflow-hidden bg-stone-950 sm:grid sm:grid-cols-2">
                <div className="p-8 md:p-12 lg:px-16 lg:py-24">
                    <div className="mx-auto max-w-xl text-center ltr:sm:text-left rtl:sm:text-right flex justify-center items-center min-h-[60vh]">
                        <div>
                            <h2 className="text-2xl font-bold text-gray-400 md:text-3xl">
                                Do you need to tell us something?
                            </h2>

                            <p className="hidden text-gray-100 md:mt-4 md:block leading-relaxed">
                                We&apos;re here to help! Whether you have questions, need support, or want to learn more about how Cobex can help your cooperative thrive, feel free to reach out to us. Fill the form below, we look forward to hearing from you and helping your cooperative grow!


                            </p>

                            <div className="mt-4 md:mt-8">
                                <Link className="inline-block rounded bg-themeThree px-12 py-3 text-sm font-medium text-white transition hover:bg-themeTwo focus:outline-none focus:ring focus:ring-themeTwo" to="/auth/register"> Get Started Today </Link>
                            </div>
                        </div>
                    </div>
                </div>

                <img
                    alt=""
                    src="/assets/images/contact.jpg"
                    className="h-56 w-full object-cover sm:h-full"
                />
            </section>

            <div className="max-w-[85rem] px-4 py-16 sm:px-6 lg:py-20 mx-auto bg-neutral-900 md:px-32 min-h-[100vh]">
                <div className="max-w-xl mx-auto">
                    <div className="text-center">
                        <h1 className="text-3xl font-bold text-gray-100 sm:text-4xl">
                            Contact us
                        </h1>
                        <p className="mt-1 text-gray-600">
                            We'd love to talk about how we can help you.
                        </p>
                    </div>
                </div>

                <div className="mt-12 max-w-lg mx-auto bg-stone-950">
                    <div className="flex flex-col border rounded-xl p-4 sm:p-6 lg:p-8">
                        <h2 className="mb-8 text-xl font-semibold text-gray-400">
                            Fill in the form
                        </h2>

                        <form>
                            <div className="grid gap-4 lg:gap-6">
                                <div className="grid grid-cols-1 sm:grid-cols-2 gap-4 lg:gap-6">
                                    <div>
                                        <label htmlFor="hs-firstname-contacts-1" className="block mb-2 text-sm text-gray-400 font-medium">First Name</label>
                                        <input type="text" name="hs-firstname-contacts-1" id="hs-firstname-contacts-1" className="py-3 px-4 block w-full border-gray-200 rounded-lg text-sm focus:border-themeThree focus:ring-themeThree disabled:opacity-50 disabled:pointer-events-none" />
                                    </div>

                                    <div>
                                        <label htmlFor="hs-lastname-contacts-1" className="block mb-2 text-sm text-gray-400 font-medium">Last Name</label>
                                        <input type="text" name="hs-lastname-contacts-1" id="hs-lastname-contacts-1" className="py-3 px-4 block w-full border-gray-200 rounded-lg text-sm focus:border-themeThree focus:ring-themeThree disabled:opacity-50 disabled:pointer-events-none" />
                                    </div>
                                </div>

                                <div className="grid grid-cols-1 sm:grid-cols-2 gap-4 lg:gap-6">
                                    <div>
                                        <label htmlFor="hs-email-contacts-1" className="block mb-2 text-sm text-gray-400 font-medium">Email</label>
                                        <input type="email" name="hs-email-contacts-1" id="hs-email-contacts-1" autoComplete="email" className="py-3 px-4 block w-full border-gray-200 rounded-lg text-sm focus:border-themeThree focus:ring-themeThree disabled:opacity-50 disabled:pointer-events-none" />
                                    </div>

                                    <div>
                                        <label htmlFor="hs-phone-number-1" className="block mb-2 text-sm text-gray-400 font-medium">Phone Number</label>
                                        <input type="text" name="hs-phone-number-1" id="hs-phone-number-1" className="py-3 px-4 block w-full border-gray-200 rounded-lg text-sm focus:border-themeThree focus:ring-themeThree disabled:opacity-50 disabled:pointer-events-none" />
                                    </div>
                                </div>

                                <div>
                                    <label htmlFor="hs-about-contacts-1" className="block mb-2 text-sm text-gray-400 font-medium">Details</label>
                                    <textarea id="hs-about-contacts-1" name="hs-about-contacts-1" rows={4} className="py-3 px-4 block w-full border-gray-200 rounded-lg text-sm focus:border-themeThree focus:ring-themeThree disabled:opacity-50 disabled:pointer-events-none"></textarea>
                                </div>
                            </div>

                            <div className="mt-6 grid">
                                <button type="submit" className="w-full py-3 px-4 inline-flex justify-center items-center gap-x-2 text-sm font-medium rounded-lg border border-transparent bg-themeThree text-white hover:bg-themeTwo focus:outline-none focus:bg-themeTwo disabled:opacity-50 disabled:pointer-events-none">Send inquiry</button>
                            </div>

                            <div className="mt-3 text-center">
                                <p className="text-sm text-gray-500">
                                    We'll get back to you in 1-2 business days.
                                </p>
                            </div>
                        </form>
                    </div>
                </div>

                <div className="mt-12 grid sm:grid-cols-2 lg:grid-cols-3 items-center gap-4 lg:gap-8">
                    <a className="group flex flex-col h-full text-center rounded-lg hover:bg-neutral-950 focus:outline-none focus:bg-neutral-950 p-4 sm:p-6" href="#">
                        <svg className="size-9 text-gray-400 mx-auto" xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round"><circle cx="12" cy="12" r="10" /><path d="M9.09 9a3 3 0 0 1 5.83 1c0 2-3 3-3 3" /><path d="M12 17h.01" /></svg>
                        <div className="mt-5">
                            <h3 className="text-lg font-semibold text-gray-400">Knowledgebase</h3>
                            <p className="mt-1 text-gray-200">We're here to help with any questions or code.</p>
                            <p className="mt-5 inline-flex items-center gap-x-1 font-medium text-themeThree">
                                Contact support
                                <svg className="shrink-0 size-4 transition ease-in-out group-hover:translate-x-1 group-focus:translate-x-1" xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round"><path d="m9 18 6-6-6-6" /></svg>
                            </p>
                        </div>
                    </a>

                    <a className="group flex flex-col h-full text-center rounded-lg hover:bg-neutral-950 focus:outline-none focus:bg-neutral-950 p-4 sm:p-6" href="#">
                        <svg className="size-9 text-gray-400 mx-auto" xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round"><path d="M14 9a2 2 0 0 1-2 2H6l-4 4V4c0-1.1.9-2 2-2h8a2 2 0 0 1 2 2v5Z" /><path d="M18 9h2a2 2 0 0 1 2 2v11l-4-4h-6a2 2 0 0 1-2-2v-1" /></svg>
                        <div className="mt-5">
                            <h3 className="text-lg font-semibold text-gray-400">FAQ</h3>
                            <p className="mt-1 text-gray-200">Search our FAQ for answers to anything you might ask.</p>
                            <p className="mt-5 inline-flex items-center gap-x-1 font-medium text-themeThree">
                                Visit FAQ
                                <svg className="shrink-0 size-4 transition ease-in-out group-hover:translate-x-1 group-focus:translate-x-1" xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round"><path d="m9 18 6-6-6-6" /></svg>
                            </p>
                        </div>
                    </a>

                    <a className="group flex flex-col h-full text-center rounded-lg hover:bg-neutral-950 focus:outline-none focus:bg-neutral-950 p-4 sm:p-6" href="#">
                        <svg className="size-9 text-gray-400 mx-auto" xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round"><path d="m7 11 2-2-2-2" /><path d="M11 13h4" /><rect width="18" height="18" x="3" y="3" rx="2" ry="2" /></svg>
                        <div className="mt-5">
                            <h3 className="text-lg font-semibold text-gray-400">Developer APIs</h3>
                            <p className="mt-1 text-gray-200">Check out our development quickstart guide.</p>
                            <p className="mt-5 inline-flex items-center gap-x-1 font-medium text-themeThree">
                                Contact sales
                                <svg className="shrink-0 size-4 transition ease-in-out group-hover:translate-x-1 group-focus:translate-x-1" xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round"><path d="m9 18 6-6-6-6" /></svg>
                            </p>
                        </div>
                    </a>
                </div>
            </div>
            <Footer />
        </>
    )
}

export default Contact