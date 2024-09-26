import { Link } from "react-router-dom"

interface OrganisationSideProps {
    activeLink1?: string;
    activeLink2?: string;
    activeLink3?: string;
}

const OrganisationSide: React.FC<OrganisationSideProps> = ({ activeLink1, activeLink2, activeLink3 }) => {
    return (
        <>
            <div
                className="grid gap-6 text-normal font-semibold text-muted-foreground" x-chunk="dashboard-04-chunk-0"
            >
                <Link to="/overview" className={`${activeLink1} text-primary`}>
                    Organisation
                </Link>
                <Link to="/organisation/details" className={`${activeLink2} text-primary`}>Details</Link>
                <Link to="/organisation/settings" className={`${activeLink3} text-primary`}>Settings</Link>
            </div >
        </>
    )
}

export default OrganisationSide