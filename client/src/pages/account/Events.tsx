import Footer from "@/components/Footer"
import InnerHeader from "@/components/InnerHeader"
import {
    CreditCard, Users
} from "lucide-react"

import {
    Card,
    CardContent,
    CardFooter,
    CardHeader,
    CardTitle,
} from "@/components/ui/card"
import { HiCalendar, HiCash } from "react-icons/hi"
import { Input } from "@/components/ui/input"

const Events = () => {
    return (
        <>
            <InnerHeader />

            <div className="bg-gradient-to-b from-slate-400 via-cyan-100 to-green-200 w-full">

                <div className="px-10 py-10">
                    <div>
                        <div className="flex min-h-screen w-full flex-col">
                            <main className="flex flex-1 flex-col gap-4 p-4 md:gap-8 md:p-8">
                                <div className="grid gap-4 md:grid-cols-2 md:gap-8 lg:grid-cols-4">
                                    <Card x-chunk="dashboard-01-chunk-0" className="bg-green-950 text-white border-gray-700">
                                        <CardHeader className="flex flex-row items-center justify-between space-y-0 pb-2">
                                            <CardTitle className="text-sm font-medium">
                                                Upcoming Events
                                            </CardTitle>
                                            <HiCalendar className="h-4 w-4 text-muted-foreground" />
                                        </CardHeader>
                                        <CardContent>
                                            <div className="text-2xl font-bold">0</div>
                                        </CardContent>
                                    </Card>
                                    <Card x-chunk="dashboard-01-chunk-1" className="bg-emerald-950 text-white border-gray-700">
                                        <CardHeader className="flex flex-row items-center justify-between space-y-0 pb-2">
                                            <CardTitle className="text-sm font-medium">
                                                Your Organisation(s)
                                            </CardTitle>
                                            <Users className="h-4 w-4 text-muted-foreground" />
                                        </CardHeader>
                                        <CardContent>
                                            <div className="text-2xl font-bold">0</div>
                                        </CardContent>
                                    </Card>
                                    <Card x-chunk="dashboard-01-chunk-2" className="bg-teal-950 text-white border-gray-700">
                                        <CardHeader className="flex flex-row items-center justify-between space-y-0 pb-2">
                                            <CardTitle className="text-sm font-medium">Unpaid Levies</CardTitle>
                                            <CreditCard className="h-4 w-4 text-muted-foreground" />
                                        </CardHeader>
                                        <CardContent>
                                            <div className="text-2xl font-bold">0</div>
                                        </CardContent>
                                    </Card>
                                    <Card x-chunk="dashboard-01-chunk-3" className="bg-cyan-950 text-white border-gray-700">
                                        <CardHeader className="flex flex-row items-center justify-between space-y-0 pb-2">
                                            <CardTitle className="text-sm font-medium">Overdue Levies</CardTitle>
                                            <HiCash className="h-4 w-4 text-muted-foreground" />
                                        </CardHeader>
                                        <CardContent>
                                            <div className="text-2xl font-bold">0</div>
                                        </CardContent>
                                    </Card>
                                </div>
                                <div className="grid gap-4">
                                    <Card x-chunk="dashboard-01-chunk-0" className="bg-green-950 text-white border-gray-700">
                                        <CardHeader className="flex flex-row items-center justify-between space-y-0 pb-2">
                                            <CardTitle className="text-xl font-bold">
                                                Create an Event
                                            </CardTitle>
                                        </CardHeader>
                                        <CardContent>
                                            <form>
                                                <CardContent className="grid grid-cols-2 gap-8">
                                                    <div>
                                                        <label htmlFor="title" className="text-lg font-semibold py-2"> Title</label>
                                                        <Input type="text" name="title" id="title" />
                                                    </div>

                                                    <div>
                                                        <label htmlFor="date" className="text-lg font-semibold py-2"> Date of Event</label>
                                                        <Input type="date" name="date" id="date" />
                                                    </div>
                                                    <div>
                                                        <label htmlFor="description" className="text-lg font-semibold py-2"> Event Description</label>
                                                        <Input type="text" name="description" id="description" />
                                                    </div>
                                                    <div>
                                                        <label htmlFor="image" className="text-lg font-semibold py-2"> Image</label>
                                                        <Input type="file" name="image" id="image" />
                                                    </div>
                                                </CardContent>
                                                <CardFooter className="border-t px-6 py-4 border-slate-500 gap-4">
                                                    <button className="bg-primary text-primary-foreground hover:bg-primary/90 h-10 px-4 py-2 rounded-md font-semibold" type="submit">Create</button>
                                                </CardFooter>
                                            </form>
                                        </CardContent>
                                    </Card>
                                </div>

                                <div className="grid grid-cols-3 gap-4">
                                    <div className="py-8">
                                        <div className="bg-neutral-900 rounded-xl max-h-full">
                                            <div>
                                                <img className="object-cover rounded-t-xl" src="assets/images/society-1.jpg" alt="" />
                                            </div>
                                            <div className="p-4">
                                                <div className="grid grid-cols-3 gap-1 text-white py-4">
                                                    <div className="col-span-2 flex items-center text-left">
                                                        <p className="font-normal text-sm leading-normal">Annual General Meeting</p>
                                                    </div>
                                                </div>
                                                <div className="text-white text-base text-left py-4">
                                                    <p>We are excited to announce our Annual Meeting, where we will review the past year’s progress, set goals for the future, and engage in meaningful discussions with stakeholders. This event provides a great opportunity for collaboration, networking, and planning. Join us as we reflect on achievements and plan ahead for continued growth and success.</p>
                                                </div>
                                                <div className="text-white text-base text-left py-4">
                                                    <p>{new Date().toDateString()}</p>
                                                </div>
                                            </div>
                                        </div>
                                    </div>
                                </div>
                            </main>
                        </div>
                    </div>
                </div >
            </div >
            <Footer />
        </>
    )
}

export default Events