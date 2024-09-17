import { Link } from "react-router-dom"
import Footer from "../components/Footer"
import Header from "../components/Header"


const Learn = () => {
    return (
        <>
            <Header />

            <div className="max-w-[85rem] py-10 sm:px-6 lg:py-14 mx-auto bg-stone-950 md:px-32">
                <div className="lg:grid lg:grid-cols-12 lg:gap-16 lg:items-center">
                    <div className="lg:col-span-7">
                        <div className="grid grid-cols-12 gap-2 sm:gap-6 items-center lg:-translate-x-10">
                            <div className="col-span-4">
                                <img className="rounded-xl" src="https://images.unsplash.com/photo-1606868306217-dbf5046868d2?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=920&q=80" alt="Features Image" />
                            </div>

                            <div className="col-span-3">
                                <img className="rounded-xl" src="https://images.unsplash.com/photo-1605629921711-2f6b00c6bbf4?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=920&q=80" alt="Features Image" />
                            </div>

                            <div className="col-span-5">
                                <img className="rounded-xl" src="https://images.unsplash.com/photo-1600194992440-50b26e0a0309?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=920&q=80" alt="Features Image" />
                            </div>
                        </div>
                    </div>

                    <div className="mt-5 sm:mt-10 lg:mt-0 lg:col-span-5">
                        <div className="space-y-6 sm:space-y-8">
                            <div className="space-y-2 md:space-y-4">
                                <h2 className="font-bold text-3xl lg:text-4xl text-gray-400">
                                    Collaborative Tools for Streamlining Cooperative Management
                                </h2>
                                <p className="text-gray-100 leading-relaxed">
                                    Leverage Cobex's tools to explore new ideas for improving your cooperative's operations. Design and manage your cooperative effortlessly, then share reports and insights with ease.

                                </p>
                            </div>

                            <ul className="space-y-2 sm:space-y-4">
                                <li className="flex gap-x-3">
                                    <span className="mt-0.5 size-5 flex justify-center items-center rounded-full bg-blue-50 text-themeThree">
                                        <svg className="shrink-0 size-3.5" xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><polyline points="20 6 9 17 4 12" /></svg>
                                    </span>
                                    <div className="grow">
                                        <span className="text-sm sm:text-base text-gray-100">
                                            <span className="font-bold">Less routine</span> – more impact
                                        </span>
                                    </div>
                                </li>

                                <li className="flex gap-x-3">
                                    <span className="mt-0.5 size-5 flex justify-center items-center rounded-full bg-blue-50 text-themeThree">
                                        <svg className="shrink-0 size-3.5" xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><polyline points="20 6 9 17 4 12" /></svg>
                                    </span>
                                    <div className="grow">
                                        <span className="text-sm sm:text-base text-gray-100">
                                            Significant Savings for Cooperatives
                                        </span>
                                    </div>
                                </li>

                                <li className="flex gap-x-3">
                                    <span className="mt-0.5 size-5 flex justify-center items-center rounded-full bg-blue-50 text-themeThree">
                                        <svg className="shrink-0 size-3.5" xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><polyline points="20 6 9 17 4 12" /></svg>
                                    </span>
                                    <div className="grow">
                                        <span className="text-sm sm:text-base text-gray-100">
                                            Scale budgets <span className="font-bold">efficiently</span>
                                        </span>
                                    </div>
                                </li>
                            </ul>
                        </div>
                    </div>
                </div>
            </div>

            <section className="bg-neutral-900">
                <div className="mx-auto max-w-screen-xl px-4 py-8 sm:px-6 sm:py-12 md:px-32 lg:py-16">
                    <div className="grid grid-cols-1 gap-8 lg:grid-cols-2 lg:gap-16">
                        <div className="relative h-64 overflow-hidden rounded-lg sm:h-80 lg:order-last lg:h-full">
                            <img
                                alt=""
                                src="/assets/images/learn-more-pr.jpg"
                                className="absolute inset-0 h-full w-full object-cover"
                            />
                        </div>

                        <div className="lg:py-24">
                            <h2 className="text-3xl font-bold sm:text-4xl text-gray-400">Manage Your Cooperative with Zero Upfront Costs</h2>

                            <p className="mt-4 text-gray-100 leading-relaxed">
                                Cobex is completely free to use, allowing you to manage and grow your cooperative without any initial fees. We only charge a 5% fee on each transaction made through the platform, so you can focus on expanding your community while we handle the rest.
                            </p>

                            <Link className="mt-8 inline-block rounded bg-themeThree px-12 py-3 text-sm font-medium text-white transition hover:bg-themeTwo focus:outline-none focus:ring focus:ring-themeTwo tracking-wider" to="/auth/register"> Get Started Today </Link>
                        </div>
                    </div>
                </div>
            </section>

            <div className="max-w-[85rem] px-4 py-10 sm:px-6 lg:py-14 mx-auto bg-stone-950 md:px-32">
                <div className="aspect-w-16 aspect-h-7 hover:cursor-pointer">
                    <img className="w-full object-cover rounded-xl max-h-screen grayscale hover:grayscale-0 hover:scale-[0.97] hover:-hue-rotate-60 transition ease-in-out delay-150 duration-300" src="/assets/images/learn-more.jpg" alt="Features Image" />
                </div>

                <div className="mt-5 lg:mt-16 grid lg:grid-cols-3 gap-8 lg:gap-12">
                    <div className="lg:col-span-1">
                        <h2 className="font-bold text-2xl md:text-3xl text-gray-500">
                            Empowering Cooperative Societies
                        </h2>
                        <p className="mt-2 md:mt-4 text-gray-100 leading-relaxed">
                            At Cobex, we address the unique challenges faced by cooperative societies. Beyond providing digital solutions for cooperative management, we&apos;ve developed tailored products to solve common pain points identified through our projects and experience.
                        </p>
                    </div>

                    <div className="lg:col-span-2">
                        <div className="grid sm:grid-cols-2 gap-8 md:gap-12">
                            <div className="flex gap-x-5">
                                <svg className="shrink-0 mt-1 size-6 text-themeThree" xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect width="18" height="10" x="3" y="11" rx="2" /><circle cx="12" cy="5" r="2" /><path d="M12 7v4" /><line x1="8" x2="8" y1="16" y2="16" /><line x1="16" x2="16" y1="16" y2="16" /></svg>
                                <div className="grow">
                                    <h3 className="text-lg font-semibold text-gray-400">
                                        Innovative Teams
                                    </h3>
                                    <p className="mt-1 text-gray-100 leading-relaxed">
                                        Our success lies in our people. We carefully select our teams, bringing together innovative minds to deliver exceptional results.
                                    </p>
                                </div>
                            </div>

                            <div className="flex gap-x-5">
                                <svg className="shrink-0 mt-1 size-6 text-themeThree" xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M7 10v12" /><path d="M15 5.88 14 10h5.83a2 2 0 0 1 1.92 2.56l-2.33 8A2 2 0 0 1 17.5 22H4a2 2 0 0 1-2-2v-8a2 2 0 0 1 2-2h2.76a2 2 0 0 0 1.79-1.11L12 2h0a3.13 3.13 0 0 1 3 3.88Z" /></svg>
                                <div className="grow">
                                    <h3 className="text-lg font-semibold text-gray-400">
                                        Simple and Affordable Solutions
                                    </h3>
                                    <p className="mt-1 text-gray-100 leading-relaxed">
                                        Cobex offers a seamless experience for managing all cooperative activities, from membership to transactions, ensuring simplicity and affordability.
                                    </p>
                                </div>
                            </div>

                            <div className="flex gap-x-5">
                                <svg className="shrink-0 mt-1 size-6 text-themeThree" xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M2 3h6a4 4 0 0 1 4 4v14a3 3 0 0 0-3-3H2z" /><path d="M22 3h-6a4 4 0 0 0-4 4v14a3 3 0 0 1 3-3h7z" /></svg>
                                <div className="grow">
                                    <h3 className="text-lg font-semibold text-gray-400">
                                        Comprehensive Documentation
                                    </h3>
                                    <p className="mt-1 text-gray-100 leading-relaxed">
                                        Our industry-leading documentation and resource libraries provide everything a cooperative needs to easily integrate and make the most of Cobex.
                                    </p>
                                </div>
                            </div>

                            <div className="flex gap-x-5">
                                <svg className="shrink-0 mt-1 size-6 text-themeThree" xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M16 21v-2a4 4 0 0 0-4-4H6a4 4 0 0 0-4 4v2" /><circle cx="9" cy="7" r="4" /><path d="M22 21v-2a4 4 0 0 0-3-3.87" /><path d="M16 3.13a4 4 0 0 1 0 7.75" /></svg>
                                <div className="grow">
                                    <h3 className="text-lg font-semibold text-gray-400">
                                        Designing with Purpose
                                    </h3>
                                    <p className="mt-1 text-gray-100 leading-relaxed">
                                        We strive for the perfect balance between functionality and user experience, ensuring Cobex is both practical and intuitive, creating seamless experiences for all users.
                                    </p>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
            <Footer />
        </>
    )
}

export default Learn