import Footer from "@/components/Footer"
import InnerHeader from "@/components/InnerHeader"
import Layout from "./Layout"



const Dashboard = () => {
    return (
        <>
            <InnerHeader />
            <div className="bg-white">
                <Layout />
            </div>
            <Footer />

        </>
    )
}

export default Dashboard