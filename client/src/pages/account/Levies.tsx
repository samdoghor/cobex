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
import {
    Select,
    SelectContent,
    SelectGroup,
    SelectItem,
    SelectLabel,
    SelectTrigger,
    SelectValue,
} from "@/components/ui/select"
import {
    Table,
    TableBody,
    TableCell,
    TableHead,
    TableHeader,
    TableRow,
} from "@/components/ui/table"

const Levies = () => {
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
                                                Create a Levy
                                            </CardTitle>
                                        </CardHeader>
                                        <CardContent>
                                            <form>
                                                <CardContent className="grid grid-cols-2 gap-8">
                                                    <div>
                                                        <label htmlFor="levy_name" className="text-lg font-semibold py-2"> Levy Name</label>
                                                        <Input type="text" name="levy_name" id="levy_name" />
                                                    </div>

                                                    <div>
                                                        <label htmlFor="interval" className="text-lg font-semibold py-2"> Intervals </label>
                                                        <Select>
                                                            <SelectTrigger className="bg-stone-950">
                                                                <SelectValue placeholder="Select Intervals" />
                                                            </SelectTrigger>
                                                            <SelectContent>
                                                                <SelectGroup>
                                                                    <SelectLabel>Intervals</SelectLabel>
                                                                    <SelectItem value="hourly">Hourly</SelectItem>
                                                                    <SelectItem value="daily">Daily</SelectItem>
                                                                    <SelectItem value="weekly">Weekly</SelectItem>
                                                                    <SelectItem value="monhtly">Monthly</SelectItem>
                                                                    <SelectItem value="annually">Annually</SelectItem>
                                                                </SelectGroup>
                                                            </SelectContent>
                                                        </Select>
                                                    </div>

                                                    <div>
                                                        <label htmlFor="amount" className="text-lg font-semibold py-2"> Amount</label>
                                                        <Input type="text" name="amount" id="amount" />
                                                    </div>
                                                </CardContent>
                                                <CardFooter className="border-t px-6 py-4 border-slate-500 gap-4">
                                                    <button className="bg-primary text-primary-foreground hover:bg-primary/90 h-10 px-4 py-2 rounded-md font-semibold" type="submit">Create</button>
                                                </CardFooter>
                                            </form>
                                        </CardContent>
                                    </Card>
                                </div>

                                <div className="py-8">
                                    <Table>
                                        <TableHeader>
                                            <TableRow>
                                                <TableHead>Levy Name</TableHead>
                                                <TableHead>Intervals</TableHead>
                                                <TableHead>Amount</TableHead>
                                                <TableHead>Started</TableHead>
                                                <TableHead>Status</TableHead>
                                                <TableHead></TableHead>
                                            </TableRow>
                                        </TableHeader>
                                        <TableBody>
                                            <TableRow>
                                                <TableCell>Monthly Dues</TableCell>
                                                <TableCell>Monthly</TableCell>
                                                <TableCell>₦2,000</TableCell>
                                                <TableCell>{new Date().toDateString()}</TableCell>
                                                <TableCell>Not Paid</TableCell>
                                                <TableCell>Make Payment</TableCell>
                                            </TableRow>
                                        </TableBody>
                                    </Table>
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

export default Levies