import Footer from "@/components/Footer"
import InnerHeader from "@/components/InnerHeader"
import OrganisationSide from "@/components/OrganisationSide"
import OrganisationTitle from "@/components/OrganisationTitle"
// import { useMember } from "@/hooks/useMember";
// import { useOrganisation } from "@/hooks/useOrganisation";
import { Button } from "@/components/ui/button"
import {
    Card,
    CardContent,
    CardFooter,
    CardHeader,
    CardTitle,
} from "@/components/ui/card"
import { Input } from "@/components/ui/input"

const OrganisationSetting = () => {
    return (
        <>
            <InnerHeader />
            <div className="flex min-h-screen w-full flex-col bg-gradient-to-b from-slate-200 to-slate-300">
                <main className="flex min-h-[calc(100vh_-_theme(spacing.16))] flex-1 flex-col gap-4 bg-muted/40 p-4 md:gap-8 md:p-10">
                    <OrganisationTitle page="/settings" />
                    <div className="mx-auto grid w-full max-w-6xl items-start gap-6 md:grid-cols-[180px_1fr] lg:grid-cols-[250px_1fr]">
                        <OrganisationSide
                            activeLink1="font-normal"
                            activeLink2="font-semibold"
                        />
                        <div className="grid gap-6">

                            <Card x-chunk="dashboard-04-chunk-1" className="bg-gradient-to-r from-slate-400 to-gray-400">
                                <CardHeader>
                                    <CardTitle>First Name</CardTitle>
                                </CardHeader>
                                <form>
                                    <CardContent>
                                        <Input type="text" name="first_name" id="first_name" />
                                    </CardContent>
                                    <CardFooter className="border-t px-6 py-4 border-slate-500 gap-4">
                                        <button className="bg-primary text-primary-foreground hover:bg-primary/90 h-10 px-4 py-2 rounded-md font-semibold" type="submit">Save</button>
                                        <Button>Cancel</Button>
                                    </CardFooter>
                                </form>
                            </Card>

                        </div>
                    </div>
                </main>
            </div>
            <Footer />
        </>
    )
}

export default OrganisationSetting