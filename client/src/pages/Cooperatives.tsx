import { Link } from "react-router-dom"
import Footer from "../components/Footer"
import Header from "../components/Header"
import SparklesText from "../components/magicui/sparkles-text"
import ShinyButton from "../components/magicui/shiny-button"
import { useOrganisation } from "../hooks/useOrganisation"
import Loading from "../components/Loading"

const Cooperatives = () => {
    const { data, isLoading, isError } = useOrganisation();

    return (
        <>
            <Header />
            <div className="relative overflow-hidden before:absolute before:top-0 before:start-1/2 before:bg-[url('https://preline.co/assets/svg/examples/polygon-bg-element.svg')] before:bg-no-repeat before:bg-top before:bg-cover before:size-full before:-z-[1] before:transform before:-translate-x-1/2 bg-stone-950">
                <div className="max-w-[85rem] mx-auto px-4 sm:px-6 lg:px-8 pt-24 pb-10">
                    <div className="mt-5 max-w-2xl text-center mx-auto flex items-center justify-center">
                        <h1 className="block font-bold text-gray-400 text-4xl md:text-5xl lg:text-6xl">
                            Grow
                        </h1>
                        <SparklesText text="Together" className="ps-2 text-gray-400" />

                    </div>

                    <div className="max-w-3xl text-center mx-auto">
                        <p className="text-base leading-relaxed text-gray-100">Cobex streamlines cooperative management by automating member contributions, loan tracking, and transaction transparency. It enhances efficiency while charging only 5% per transaction.</p>
                    </div>

                    <div className="mt-8 gap-3 flex justify-center">
                        <Link className="inline-flex justify-center items-center gap-x-3 text-center bg-gradient-to-tl from-themeThree to-themeTwo hover:from-themeTwo hover:to-themeThree border border-transparent text-white text-sm font-medium rounded-md focus:outline-none focus:from-themeTwo focus:to-themeThree py-3 px-4" to="/auth/register">
                            Create an Account
                            <svg className="shrink-0 size-4" xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round"><path d="m9 18 6-6-6-6" /></svg>
                        </Link>
                    </div>
                </div>
            </div>

            <div className="max-w-[85rem] px-4 py-10 sm:px-6 md:px-8 lg:py-14 mx-auto bg-stone-950">
                <div className="grid grid-cols-12 items-center gap-x-2 sm:gap-x-6 lg:gap-x-8 md:px-32">
                    <div className="hidden md:block col-span-4 md:col-span-3">
                        <img className="rounded-xl hover:grayscale hover:cursor-pointer" src="/assets/images/society-1.jpg" alt="Features Image" />
                    </div>

                    <div className="col-span-4 md:col-span-3">
                        <img className="rounded-xl hover:grayscale hover:cursor-pointer" src="/assets/images/society-2.jpg" alt="Features Image" />
                    </div>

                    <div className="col-span-4 md:col-span-3">
                        <img className="rounded-xl hover:grayscale hover:cursor-pointer" src="/assets/images/society-3.jpg" alt="Features Image" />
                    </div>

                    <div className="col-span-4 md:col-span-3">
                        <img className="rounded-xl hover:grayscale hover:cursor-pointer" src="/assets/images/society-4.jpg" alt="Features Image" />
                    </div>
                </div>

                <div className="mx-auto text-left mt-24 md:px-32">
                    <h2 className="text-3xl lg:text-4xl text-gray-400 font-bold">
                        Registered Cooperatives
                    </h2>
                    <p className="mt-3 text-gray-100">
                        Look through every cooperative we have if you can see yours.
                    </p>
                </div>
            </div>

            <div className="max-w-[85rem] md:px-40 sm:px-6 py-20 mx-auto bg-neutral-950 min-h-screen">
                {isLoading ? (
                    <Loading />
                ) : isError ? (
                    <div>Error loading data.</div>
                ) : (
                    <div className="grid grid-cols-3 gap-4">
                        {data?.data.map((organisation) => (
                            <div key={organisation.id} className="bg-neutral-900 rounded-xl max-h-full">
                                <div>
                                    <img className="object-cover rounded-t-xl" src="assets/images/society-1.jpg" alt="" />
                                </div>
                                <div className="p-4">
                                    <div className="grid grid-cols-3 gap-1 text-white py-4">
                                        <div className="flex items-center">
                                            <img className="w-20 h-20 object-cover rounded-full" src="assets/images/society-1.jpg" alt="" />
                                        </div>
                                        <div className="col-span-2 flex items-center text-left">
                                            <p className="font-normal text-sm leading-normal">{organisation.full_name}</p>
                                        </div>
                                    </div>
                                    <div className="text-white text-base text-left py-4">
                                        <p>{organisation.short_name}</p>
                                    </div>
                                    {/* <div className="text-white text-base text-left py-4">
                                        <p>{organisation.state}, {organisation.country} </p>
                                    </div> */}
                                    <div className="grid grid-cols-2 gap-4 border-t border-gray-700 pt-4">
                                        <div className="flex items-center justify-center">
                                            <ShinyButton text="Details" className="text-white text-center bg-themeTwo hover:bg-themeOne py-2 px-4 rounded-lg text-sm font-normal" />
                                        </div>
                                        <div className="flex items-center justify-center">
                                            <ShinyButton text="Message" className="text-white text-center bg-themeTwo hover:bg-themeOne py-2 px-4 rounded-lg text-sm font-normal" />
                                        </div>
                                    </div>
                                </div>
                            </div>
                        ))}
                    </div>
                )}
            </div>


            <Footer />
        </>
    )
}

export default Cooperatives