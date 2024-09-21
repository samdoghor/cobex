import Footer from "@/components/Footer"
import InnerHeader from "@/components/InnerHeader"
import { Button } from "@/components/ui/button"
import {
    Card,
    CardContent,
    CardDescription,
    CardFooter,
    CardHeader,
    CardTitle,
} from "@/components/ui/card"
import { Input } from "@/components/ui/input"

const Profile = () => {
    return (
        <>

            <InnerHeader />
            <div className="bg-neutral-900 w-full min-h-screen md:px-32">
                <div className="py-8">
                    <p className="text-white font-bold text-4xl tracking-wider">Profile</p>
                </div>

                <div className="py-8">
                    <Card className="bg-stone-950">
                        <CardHeader>
                            <CardTitle className="text-white">Bio Data</CardTitle>
                            <CardDescription>
                                Used to identify your store in the marketplace.
                            </CardDescription>
                        </CardHeader>
                        <CardContent>
                            <form>
                                <div className="grid grid-cols-2 gap-8">
                                    <div className="py-2">
                                        <div className="py-4">
                                            <label htmlFor="first_name" className="text-white pb-4"> First Name </label>
                                        </div>
                                        <Input type="text" name="first_name" id="first_name" disabled value="" className="py-3 px-4 block w-full border-gray-200 rounded-lg text-sm focus:border-blue-500 focus:ring-blue-500 disabled:opacity-50 disabled:pointer-events-none" />
                                    </div>
                                    <div className="py-2">
                                        <div className="py-4">
                                            <label htmlFor="last_name" className="text-white pb-4"> Last Name </label>
                                        </div>
                                        <Input type="text" name="last_name" id="last_name" disabled value="" className="py-3 px-4 block w-full border-gray-200 rounded-lg text-sm focus:border-blue-500 focus:ring-blue-500 disabled:opacity-50 disabled:pointer-events-none" />
                                    </div>
                                </div>

                                <div className="grid grid-cols-2 gap-8">
                                    <div className="py-2">
                                        <div className="py-4">
                                            <label htmlFor="middle_name" className="text-white pb-4"> Middle Name </label>
                                        </div>
                                        <Input type="text" name="middle_name" id="middle_name" disabled value="" className="py-3 px-4 block w-full border-gray-200 rounded-lg text-sm focus:border-blue-500 focus:ring-blue-500 disabled:opacity-50 disabled:pointer-events-none" />
                                    </div>
                                    <div className="py-2">
                                        <div className="py-4">
                                            <label htmlFor="dob" className="text-white pb-4"> Date of Birth </label>
                                        </div>
                                        <Input type="date" name="dob" id="dob" disabled value="" className="py-3 px-4 block w-full border-gray-200 rounded-lg text-sm focus:border-blue-500 focus:ring-blue-500 disabled:opacity-50 disabled:pointer-events-none" />
                                    </div>
                                </div>
                            </form>
                        </CardContent>
                        <CardFooter className="border-t px-6 py-4">
                            <Button>Save</Button>
                        </CardFooter>
                    </Card>
                </div>

                <div className="py-8">
                    <Card className="bg-stone-950">
                        <CardHeader>
                            <CardTitle className="text-white">Account Data</CardTitle>
                        </CardHeader>
                        <CardContent>
                            <form>
                                <div className="grid grid-cols-2 gap-8">
                                    <div className="py-2">
                                        <div className="py-4">
                                            <label htmlFor="email" className="text-white pb-4"> Email Address </label>
                                        </div>
                                        <Input type="email" name="email" id="email" disabled value="" className="py-3 px-4 block w-full border-gray-200 rounded-lg text-sm focus:border-blue-500 focus:ring-blue-500 disabled:opacity-50 disabled:pointer-events-none" />
                                    </div>
                                    <div className="py-2">
                                        <div className="py-4">
                                            <label htmlFor="password" className="text-white pb-4"> Password </label>
                                        </div>
                                        <Input type="password" name="password" id="password" disabled value="" className="py-3 px-4 block w-full border-gray-200 rounded-lg text-sm focus:border-blue-500 focus:ring-blue-500 disabled:opacity-50 disabled:pointer-events-none" />
                                    </div>
                                </div>
                            </form>
                        </CardContent>
                        <CardFooter className="border-t px-6 py-4">
                            <Button>Save</Button>
                        </CardFooter>
                    </Card>
                </div>


            </div>
            <Footer />
        </>
    )
}

export default Profile