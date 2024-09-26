import Footer from "@/components/Footer"
import InnerHeader from "@/components/InnerHeader"
import OrganisationSide from "@/components/OrganisationSide"
// import { useAllMember } from "@/hooks/useMember";
import { useOneOrganisation } from "@/hooks/useOrganisation";
// import { Button } from "@/components/ui/button"
import {
    Card,
    CardContent,
    // CardFooter,
    CardHeader,
    CardTitle,
} from "@/components/ui/card"
import { HiCash } from "react-icons/hi"
// import { Input } from "@/components/ui/input"
import {
    Table,
    TableBody,
    TableCell,
    TableHead,
    TableHeader,
    TableRow,
} from "@/components/ui/table"


const Organisation = () => {
    // const { data: memberData } = useAllMember();
    const { data: orgData } = useOneOrganisation();
    return (
        <>
            <InnerHeader />
            <div className="flex min-h-screen w-full flex-col bg-gradient-to-b from-slate-200 to-slate-300">
                <div className="bg-[url('/assets/images/society-1.jpg')] bg-cover bg-center h-[80vh] flex justify-center items-center ">
                    <div className="w-[60%] bg-white rounded-xl p-8">
                        <p className="text-center text-3xl font-bold">{orgData?.data.full_name.toUpperCase()}</p>
                    </div>
                </div>
                <main className="flex min-h-[calc(100vh_-_theme(spacing.16))] flex-1 flex-col gap-4 bg-muted/40 px-4 md:gap-8 md:px-10">
                    <div className="mx-auto grid w-full max-w-6xl items-start gap-6 md:grid-cols-[180px_1fr] lg:grid-cols-[250px_1fr] py-5">
                        <OrganisationSide
                            activeLink1="font-semibold"
                            activeLink2="font-normal"
                            activeLink3="font-normal"
                        />
                        <div>
                            <div className="gap-6 flex justify-center">
                                <Card x-chunk="dashboard-01-chunk-0" className="bg-stone-950 text-white border-gray-700 w-full">
                                    <CardHeader className="flex flex-row items-center justify-between space-y-0 pb-2">
                                        <CardTitle className="text-normal font-medium">
                                            Funds
                                        </CardTitle>
                                        <HiCash className="text-white text-lg" />
                                    </CardHeader>
                                    <CardContent>
                                        <div className="text-2xl font-bold">₦500,000</div>
                                    </CardContent>
                                </Card>
                            </div>
                            <div className="py-8">
                                <Table>
                                    <TableHeader>
                                        <TableRow>
                                            <TableHead></TableHead>
                                            <TableHead>Full Name</TableHead>
                                            <TableHead>Email</TableHead>
                                            <TableHead>Phone Number</TableHead>
                                            <TableHead>Role</TableHead>
                                        </TableRow>
                                    </TableHeader>
                                    <TableBody>
                                        <TableRow>
                                            <TableCell className="font-medium"><img src="/assets/images/happy-people.jpg" className='w-16 !h-16 rounded-full object-cover' /></TableCell>
                                            <TableCell>Samuel Doghor</TableCell>
                                            <TableCell>samdoghor@gmail.com</TableCell>
                                            <TableCell>08031390921</TableCell>
                                            <TableCell>President</TableCell>
                                        </TableRow>
                                    </TableBody>
                                </Table>
                            </div>
                        </div>
                        {/* <div className="grid gap-6">


                            <Card x-chunk="dashboard-04-chunk-1" className="bg-gradient-to-r from-slate-400 to-gray-400">
                                <CardHeader>
                                    <CardTitle>{orgData?.data.full_name}</CardTitle>
                                </CardHeader>
                                <CardContent>
                                    <Input type="text" name="first_name" id="first_name" />
                                </CardContent>
                                <CardFooter className="border-t px-6 py-4 border-slate-500 gap-4">
                                    <button className="bg-primary text-primary-foreground hover:bg-primary/90 h-10 px-4 py-2 rounded-md font-semibold" type="submit">Save</button>
                                    <Button>Cancel</Button>
                                </CardFooter>
                            </Card>

                        </div> */}
                    </div>
                </main>
            </div>
            <Footer />
        </>
    )
}

export default Organisation