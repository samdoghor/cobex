import { Link } from "react-router-dom"
import Footer from "../components/Footer"
import Header from "../components/Header"
import AnimatedGridPattern from "../components/magicui/animated-grid-pattern"
import ShineBorder from "../components/magicui/shine-border"
import { cn } from "../lib/utils"

const Index = () => {
    return (
        <>
            <Header />
            <div className="min-h-screen bg-gradient-to-b from-stone-950 to-neutral-950">
                <div className="flex flex-col items-center justify-center min-h-screen py-14">
                    <p className="text-white text-center mt-20">
                        <span className="whitespace-nowrap rounded-full bg-white px-6 py-2 text-xs text-themeSix font-bold tracking-wider"
                        >
                            Cooperative Society Management
                        </span>
                    </p>

                    <p className="text-white text-center text-5xl mt-8 font-bold w-[70%] leading-snug">
                        <span className=""> Manage </span> your <span className="">cooperative societies</span>, <span className="text-themeThree">seamlessly</span> and <span className="text-themeThree">transparently</span>.
                    </p>
                    <p className="text-gray-500 text-center text-xl mt-2 font-semibold">
                        Never worry about payment collection or member management.
                    </p>

                    <a className="group relative inline-block focus:outline-none focus:ring mt-20" href="#">
                        <span
                            className="absolute inset-0 translate-x-1.5 translate-y-1.5 bg-themeThree transition-transform group-hover:translate-x-0 group-hover:translate-y-0 rounded-md"
                        ></span>


                        <Link className="relative inline-block border-2 border-white rounded-md px-8 py-3 text-sm font-bold uppercase tracking-widest text-white group-active:text-opacity-75" to="/auth/register"> Get Started </Link>
                    </a>
                    <div className="bg-stone-950 min-h-screen">
                        <div className="flex flex-col items-center justify-center py-20">
                            <div className="w-8/12 hover:shadow-2xl hover:shadow-zinc-800 hover:cursor-pointer hover:scale-[0.97] transition ease-in-out delay-150 duration-300">
                                <ShineBorder
                                    className="border-2 bg-stone-950 p-2 relative flex w-full flex-col items-center justify-center overflow-hidden rounded-lg"
                                    color={["#000000", "#14aea1", "#ff0000"]}
                                >
                                    <img src="/assets/images/dashboard.png" alt="Dashboard" className="min-h-[80vh] object-cover object-left" />
                                </ShineBorder>
                            </div>
                        </div>
                    </div >
                </div>
                <AnimatedGridPattern
                    numSquares={30}
                    maxOpacity={0.1}
                    duration={3}
                    repeatDelay={1}
                    className={cn(
                        "[mask-image:radial-gradient(500px_circle_at_center,white,transparent)]",
                        "inset-x-0 inset-y-[-30%] skew-y-12 h-[200%] mt-32 w-full opacity-50",
                    )}
                />
            </div >

            <div className="">
                <div className="bg-neutral-900">
                    <div className="max-w-5xl mx-auto px-4 xl:px-0 pt-24 lg:pt-32 pb-24">
                        <h1 className="font-semibold text-white text-5xl md:text-6xl">
                            <span className="text-themeFive font-extrabold"> Cobex:</span> Digitized Cooperative Society Management
                        </h1>
                        <div className="max-w-4xl">
                            <p className="mt-5 text-neutral-400 text-lg">
                                Cobex is a Digitized Cooperative Society Management system designed to streamline cooperative activities such as member management, loan processing, and savings tracking. It offers a user-friendly interface with automated features to enhance transparency and efficiency in cooperative operations.
                            </p>
                        </div>
                    </div>
                </div>

                <div className="relative overflow-hidden py-4 bg-neutral-900">
                    <svg className="absolute -bottom-20 start-1/2 w-[1900px] transform -translate-x-1/2" width="2745" height="488" viewBox="0 0 2745 488" fill="none" xmlns="http://www.w3.org/2000/svg">
                        <path d="M0.5 330.864C232.505 403.801 853.749 527.683 1482.69 439.719C2111.63 351.756 2585.54 434.588 2743.87 487" className="stroke-neutral-700/50" stroke="currentColor" />
                        <path d="M0.5 308.873C232.505 381.81 853.749 505.692 1482.69 417.728C2111.63 329.765 2585.54 412.597 2743.87 465.009" className="stroke-neutral-700/50" stroke="currentColor" />
                        <path d="M0.5 286.882C232.505 359.819 853.749 483.701 1482.69 395.738C2111.63 307.774 2585.54 390.606 2743.87 443.018" className="stroke-neutral-700/50" stroke="currentColor" />
                        <path d="M0.5 264.891C232.505 337.828 853.749 461.71 1482.69 373.747C2111.63 285.783 2585.54 368.615 2743.87 421.027" className="stroke-neutral-700/50" stroke="currentColor" />
                        <path d="M0.5 242.9C232.505 315.837 853.749 439.719 1482.69 351.756C2111.63 263.792 2585.54 346.624 2743.87 399.036" className="stroke-neutral-700/50" stroke="currentColor" />
                        <path d="M0.5 220.909C232.505 293.846 853.749 417.728 1482.69 329.765C2111.63 241.801 2585.54 324.633 2743.87 377.045" className="stroke-neutral-700/50" stroke="currentColor" />
                        <path d="M0.5 198.918C232.505 271.855 853.749 395.737 1482.69 307.774C2111.63 219.81 2585.54 302.642 2743.87 355.054" className="stroke-neutral-700/50" stroke="currentColor" />
                        <path d="M0.5 176.927C232.505 249.864 853.749 373.746 1482.69 285.783C2111.63 197.819 2585.54 280.651 2743.87 333.063" className="stroke-neutral-700/50" stroke="currentColor" />
                        <path d="M0.5 154.937C232.505 227.873 853.749 351.756 1482.69 263.792C2111.63 175.828 2585.54 258.661 2743.87 311.072" className="stroke-neutral-700/50" stroke="currentColor" />
                        <path d="M0.5 132.946C232.505 205.882 853.749 329.765 1482.69 241.801C2111.63 153.837 2585.54 236.67 2743.87 289.082" className="stroke-neutral-700/50" stroke="currentColor" />
                        <path d="M0.5 110.955C232.505 183.891 853.749 307.774 1482.69 219.81C2111.63 131.846 2585.54 214.679 2743.87 267.091" className="stroke-neutral-700/50" stroke="currentColor" />
                        <path d="M0.5 88.9639C232.505 161.901 853.749 285.783 1482.69 197.819C2111.63 109.855 2585.54 192.688 2743.87 245.1" className="stroke-neutral-700/50" stroke="currentColor" />
                        <path d="M0.5 66.9729C232.505 139.91 853.749 263.792 1482.69 175.828C2111.63 87.8643 2585.54 170.697 2743.87 223.109" className="stroke-neutral-700/50" stroke="currentColor" />
                        <path d="M0.5 44.9819C232.505 117.919 853.749 241.801 1482.69 153.837C2111.63 65.8733 2585.54 148.706 2743.87 201.118" className="stroke-neutral-700/50" stroke="currentColor" />
                        <path d="M0.5 22.991C232.505 95.9276 853.749 219.81 1482.69 131.846C2111.63 43.8824 2585.54 126.715 2743.87 179.127" className="stroke-neutral-700/50" stroke="currentColor" />
                        <path d="M0.5 1C232.505 73.9367 853.749 197.819 1482.69 109.855C2111.63 21.8914 2585.54 104.724 2743.87 157.136" className="stroke-neutral-700/50" stroke="currentColor" />
                    </svg>

                    <div className="relative z-10 pb-8">
                        <div className="max-w-5xl px-4 xl:px-0 mx-auto">
                            <div className="mb-4">
                                <h2 className="text-neutral-400">Trusted by cooperatives, enterprise, and more than 99,000 of you</h2>
                            </div>

                            <div className="flex justify-between gap-6">
                                <div><img src="/assets/images/wolfer-studio.png" alt="Wolfer Studio" width={80} /></div>
                                <div><img src="/assets/images/avery-davis.png" alt="Avery Davis" width={80} /></div>
                                <div><img src="/assets/images/harper-russo.png" alt="Harper Russo" width={80} /></div>
                                <div><img src="/assets/images/annesa.png" alt="Annesa" width={80} /></div>
                                <div><img src="/assets/images/maria-donna.png" alt="Maria Donna" width={80} /></div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>

            <div className="min-h-screen max-w-[85rem] mx-auto md:px-32 sm:px-6 bg-stone-950">
                <div className="grid md:grid-cols-2 gap-4 md:gap-8 xl:gap-20 md:items-center">
                    <div>
                        <h1 className="block text-3xl font-bold text-gray-400 sm:text-4xl lg:text-6xl lg:leading-tight">Automate your dues collection with <span className="text-themeThree">Cobex</span></h1>
                        <p className="mt-3 text-lg text-gray-400">Streamline payments, track contributions, and enhance transparency effortlessly. Cobex automates financial processes, providing real-time updates and detailed reports for better decision-making.</p>

                        <div className="mt-7 grid gap-3 w-full sm:inline-flex">
                            <Link className="py-3 px-4 inline-flex justify-center items-center gap-x-2 text-sm font-medium rounded-lg border border-transparent bg-themeThree text-white hover:bg-themeTwo focus:outline-none focus:bg-themeTwo disabled:opacity-50 disabled:pointer-events-none" to="/auth/register">
                                Get Started
                                <svg className="shrink-0 size-4" xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round"><path d="m9 18 6-6-6-6" /></svg>
                            </Link>
                            <Link className="py-3 px-4 inline-flex justify-center items-center gap-x-2 text-sm font-medium rounded-lg border border-gray-200 bg-white text-gray-800 shadow-sm hover:bg-gray-50 focus:outline-none focus:bg-gray-50 disabled:opacity-50 disabled:pointer-events-none" to="/contact"> Contact support team </Link>
                        </div>
                    </div>

                    <div className="relative ms-4">
                        <img className="w-full rounded-md max-h-[95vh] object-cover" src="/assets/images/happy-people.jpg" alt="Hero Image" />
                        <div className="absolute inset-0 -z-[1] bg-gradient-to-tr from-gray-200 via-white/0 to-white/0 size-full rounded-md mt-4 -mb-4 me-4 -ms-4 lg:mt-6 lg:-mb-6 lg:me-6 lg:-ms-6"></div>

                        <div className="absolute bottom-0 start-0">
                            <svg className="w-2/3 ms-auto h-auto text-stone-950" width="630" height="451" viewBox="0 0 630 451" fill="none" xmlns="http://www.w3.org/2000/svg">
                                <rect x="531" y="352" width="99" height="99" fill="currentColor" />
                                <rect x="140" y="352" width="106" height="99" fill="currentColor" />
                                <rect x="482" y="402" width="64" height="49" fill="currentColor" />
                                <rect x="433" y="402" width="63" height="49" fill="currentColor" />
                                <rect x="384" y="352" width="49" height="50" fill="currentColor" />
                                <rect x="531" y="328" width="50" height="50" fill="currentColor" />
                                <rect x="99" y="303" width="49" height="58" fill="currentColor" />
                                <rect x="99" y="352" width="49" height="50" fill="currentColor" />
                                <rect x="99" y="392" width="49" height="59" fill="currentColor" />
                                <rect x="44" y="402" width="66" height="49" fill="currentColor" />
                                <rect x="234" y="402" width="62" height="49" fill="currentColor" />
                                <rect x="334" y="303" width="50" height="49" fill="currentColor" />
                                <rect x="581" width="49" height="49" fill="currentColor" />
                                <rect x="581" width="49" height="64" fill="currentColor" />
                                <rect x="482" y="123" width="49" height="49" fill="currentColor" />
                                <rect x="507" y="124" width="49" height="24" fill="currentColor" />
                                <rect x="531" y="49" width="99" height="99" fill="currentColor" />
                            </svg>
                        </div>
                    </div>
                </div>
            </div>

            <div id="faq" className="max-w-[85rem] px-4 py-10 sm:px-6 lg:px-8 lg:py-14 mx-auto bg-neutral-900 min-h-screen">
                <div className="max-w-2xl mx-auto text-center mb-10 lg:mb-14">
                    <h2 className="text-2xl font-bold md:text-3xl md:leading-tight text-gray-400">
                        Frequently Asked Questions
                    </h2>
                </div>

                <div className="max-w-5xl mx-auto">
                    <div className="grid sm:grid-cols-2 gap-6 md:gap-12">
                        <div>
                            <h3 className="text-lg font-semibold text-gray-400">
                                Can I cancel at anytime?
                            </h3>
                            <p className="mt-2 text-gray-300">
                                Yes, you can cancel anytime no questions are asked while you cancel but we would highly appreciate if you will give us some feedback.
                            </p>
                        </div>

                        <div>
                            <h3 className="text-lg font-semibold text-gray-400">
                                My team has credits. How do we use them?
                            </h3>
                            <p className="mt-2 text-gray-300">
                                Once your team signs up for a subscription plan. This is where we sit down, grab a cup of coffee and dial in the details.
                            </p>
                        </div>

                        <div>
                            <h3 className="text-lg font-semibold text-gray-400">
                                How does Preline's pricing work?
                            </h3>
                            <p className="mt-2 text-gray-300">
                                Our subscriptions are tiered. Understanding the task at hand and ironing out the wrinkles is key.
                            </p>
                        </div>

                        <div>
                            <h3 className="text-lg font-semibold text-gray-400">
                                How secure is Cobex?
                            </h3>
                            <p className="mt-2 text-gray-300">
                                Protecting the data you trust to Cobex is our first priority. This part is really crucial in keeping the project in line to completion.
                            </p>
                        </div>

                        <div>
                            <h3 className="text-lg font-semibold text-gray-400">
                                Do you offer discounts?
                            </h3>
                            <p className="mt-2 text-gray-300">
                                We've built in discounts at each tier for teams. The time has come to bring those ideas and plans to life.
                            </p>
                        </div>

                        <div>
                            <h3 className="text-lg font-semibold text-gray-400">
                                What is your refund policy?
                            </h3>
                            <p className="mt-2 text-gray-300">
                                We offer refunds. We aim high at being focused on building relationships with our clients and community.
                            </p>
                        </div>
                    </div>
                </div>
            </div>
            <Footer />
        </>
    )
}

export default Index
