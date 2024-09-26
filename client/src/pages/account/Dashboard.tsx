import Footer from "@/components/Footer"
import InnerHeader from "@/components/InnerHeader"
import {
    CreditCard, Users
} from "lucide-react"

import {
    Avatar,
    AvatarFallback,
    AvatarImage,
} from "@/components/ui/avatar"
import {
    Card,
    CardContent,
    CardHeader,
    CardTitle,
} from "@/components/ui/card"
import { HiCalendar, HiCash } from "react-icons/hi"

import { Bar, BarChart, Pie, PieChart, XAxis } from "recharts"

import {
    CardDescription,
} from "@/components//ui/card"
import {
    ChartContainer,
    ChartTooltip,
    ChartTooltipContent,
} from "@/components//ui/chart"

import { CartesianGrid } from "recharts"
import { ChartConfig } from "@/components/ui/chart"

import { Line, LineChart } from "recharts"

const chartData = [
    { month: "Jan", desktop: 186 },
    { month: "Feb", desktop: 305 },
    { month: "Mar", desktop: 237 },
    { month: "Apr", desktop: 73 },
    { month: "May", desktop: 209 },
    { month: "Jun", desktop: 214 },
    { month: "Jul", desktop: 186 },
    { month: "Aug", desktop: 305 },
    { month: "Sept", desktop: 237 },
    { month: "Oct", desktop: 73 },
    { month: "Nov", desktop: 209 },
    { month: "Dec", desktop: 214 },
]
const chartConfig = {
    desktop: {
        label: "All Cash Inflow",
        color: "#7dd3fc",
    },
} satisfies ChartConfig

const chartDataTwo = [
    { month: "Jan", desktop: 186 },
    { month: "Feb", desktop: 305 },
    { month: "Mar", desktop: 237 },
    { month: "Apr", desktop: 73 },
    { month: "May", desktop: 209 },
    { month: "Jun", desktop: 214 },
    { month: "Jul", desktop: 186 },
    { month: "Aug", desktop: 305 },
    { month: "Sept", desktop: 237 },
    { month: "Oct", desktop: 73 },
    { month: "Nov", desktop: 209 },
    { month: "Dec", desktop: 214 },
]
const chartConfigTwo = {
    desktop: {
        label: "Desktop",
        color: "#ffffff",
    },
} satisfies ChartConfig

const chartDataThree = [
    { browser: "chrome", visitors: 275, fill: "var(--color-chrome)" },
    { browser: "safari", visitors: 200, fill: "var(--color-safari)" },
    { browser: "firefox", visitors: 187, fill: "var(--color-firefox)" },
    { browser: "edge", visitors: 173, fill: "var(--color-edge)" },
    { browser: "other", visitors: 90, fill: "var(--color-other)" },
]
const chartConfigThree = {
    visitors: {
        label: "Visitors",
    },
    chrome: {
        label: "Chrome",
        color: "hsl(var(--chart-1))",
    },
    safari: {
        label: "Safari",
        color: "hsl(var(--chart-2))",
    },
    firefox: {
        label: "Firefox",
        color: "hsl(var(--chart-3))",
    },
    edge: {
        label: "Edge",
        color: "hsl(var(--chart-4))",
    },
    other: {
        label: "Other",
        color: "hsl(var(--chart-5))",
    },
} satisfies ChartConfig

const Dashboard = () => {
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

                                <div className="grid gap-4 md:gap-8 lg:grid-cols-2 xl:grid-cols-3">
                                    <Card className="xl:col-span-2 bg-teal-950 text-white border-gray-700" x-chunk="dashboard-01-chunk-4">
                                        <CardHeader>
                                            <CardTitle>Your Cash Outflow</CardTitle>
                                            <CardDescription>by month</CardDescription>
                                        </CardHeader>
                                        <CardContent>
                                            <ChartContainer config={chartConfig}>
                                                <BarChart accessibilityLayer data={chartData}>
                                                    <CartesianGrid vertical={false} />
                                                    <XAxis
                                                        dataKey="month"
                                                        tickLine={false}
                                                        tickMargin={10}
                                                        axisLine={false}
                                                        tickFormatter={(value) => value.slice(0, 3)}
                                                    />
                                                    <ChartTooltip
                                                        cursor={false}
                                                        content={<ChartTooltipContent indicator="dashed" />}
                                                    />
                                                    <Bar dataKey="desktop" fill="#7dd3fc" radius={4} />
                                                </BarChart>
                                            </ChartContainer>
                                        </CardContent>
                                    </Card>

                                    <Card x-chunk="dashboard-01-chunk-5" className="bg-cyan-950 text-white border-gray-700">
                                        <CardHeader>
                                            <CardTitle className="font-bold">Recent Transactions</CardTitle>
                                        </CardHeader>
                                        <CardContent className="grid gap-8">
                                            <div className="flex items-center gap-4">
                                                <Avatar className="hidden h-9 w-9 sm:flex">
                                                    <AvatarImage src="/avatars/01.png" alt="Avatar" />
                                                    <AvatarFallback>OM</AvatarFallback>
                                                </Avatar>
                                                <div className="grid gap-1">
                                                    <p className="text-sm font-medium leading-none">
                                                        Olivia Martin
                                                    </p>
                                                    <p className="text-sm text-muted-foreground">
                                                        olivia.martin@email.com
                                                    </p>
                                                </div>
                                                <div className="ml-auto font-medium">+$1,999.00</div>
                                            </div>

                                        </CardContent>
                                    </Card>
                                </div>

                                <div className="grid gap-4 md:grid-cols-2 md:gap-8 lg:grid-cols-4">
                                    <Card x-chunk="dashboard-01-chunk-0" className="bg-cyan-950 text-white border-gray-700">
                                        <CardHeader className="flex flex-row items-center justify-between space-y-0 pb-2">
                                            <CardTitle className="text-sm font-medium">
                                                Total Members
                                            </CardTitle>
                                        </CardHeader>
                                        <CardContent>
                                            <div className="text-2xl font-bold">0</div>
                                        </CardContent>
                                    </Card>
                                    <Card x-chunk="dashboard-01-chunk-1" className="bg-teal-950 text-white border-gray-700">
                                        <CardHeader className="flex flex-row items-center justify-between space-y-0 pb-2">
                                            <CardTitle className="text-sm font-medium">
                                                Total Events
                                            </CardTitle>
                                        </CardHeader>
                                        <CardContent>
                                            <div className="text-2xl font-bold">0</div>
                                        </CardContent>
                                    </Card>
                                    <Card x-chunk="dashboard-01-chunk-2" className="bg-emerald-950 text-white border-gray-700">
                                        <CardHeader className="flex flex-row items-center justify-between space-y-0 pb-2">
                                            <CardTitle className="text-sm font-medium">Total Transactions</CardTitle>
                                        </CardHeader>
                                        <CardContent>
                                            <div className="text-2xl font-bold">0</div>
                                        </CardContent>
                                    </Card>
                                    <Card x-chunk="dashboard-01-chunk-3" className="bg-green-950 text-white border-gray-700">
                                        <CardHeader className="flex flex-row items-center justify-between space-y-0 pb-2">
                                            <CardTitle className="text-sm font-medium">Month Transactions</CardTitle>
                                        </CardHeader>
                                        <CardContent>
                                            <div className="text-2xl font-bold">0</div>
                                        </CardContent>
                                    </Card>
                                </div>

                                <div className="grid grid-cols-2 gap-8 text-white">
                                    <Card className="bg-teal-950 text-white border-gray-700">
                                        <CardHeader>
                                            <CardTitle>Events Across Cobex</CardTitle>
                                            <CardDescription>per month</CardDescription>
                                        </CardHeader>
                                        <CardContent>
                                            <ChartContainer config={chartConfigTwo}>
                                                <LineChart
                                                    accessibilityLayer
                                                    data={chartDataTwo}
                                                    margin={{
                                                        left: 12,
                                                        right: 12,
                                                    }}
                                                >
                                                    <CartesianGrid vertical={false} />
                                                    <XAxis
                                                        dataKey="month"
                                                        tickLine={false}
                                                        axisLine={false}
                                                        tickMargin={8}
                                                        tickFormatter={(value) => value.slice(0, 3)}
                                                    />
                                                    <ChartTooltip
                                                        cursor={false}
                                                        content={<ChartTooltipContent hideLabel />}
                                                    />
                                                    <Line
                                                        dataKey="desktop"
                                                        type="natural"
                                                        stroke="var(--color-desktop)"
                                                        strokeWidth={2}
                                                        dot={false}
                                                    />
                                                </LineChart>
                                            </ChartContainer>
                                        </CardContent>
                                    </Card>

                                    <Card className="flex flex-col bg-cyan-950 text-white">
                                        <CardHeader className="items-center pb-0">
                                            <CardTitle>Top 5 City</CardTitle>
                                            <CardDescription>Cities with more Organisation</CardDescription>
                                        </CardHeader>
                                        <CardContent className="flex-1 pb-0">
                                            <ChartContainer
                                                config={chartConfigThree}
                                                className="mx-auto aspect-square max-h-[250px] pb-0 [&_.recharts-pie-label-text]:fill-foreground"
                                            >
                                                <PieChart>
                                                    <ChartTooltip content={<ChartTooltipContent hideLabel />} />
                                                    <Pie data={chartDataThree} dataKey="visitors" label nameKey="browser" />
                                                </PieChart>
                                            </ChartContainer>
                                        </CardContent>
                                    </Card>
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

export default Dashboard