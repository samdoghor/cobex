import { Link } from "react-router-dom"

interface OrganisationSideProps {
    activeLink1?: string;
    activeLink2?: string;
    activeLink3?: string;
    activeLink4?: string;
    activeLink5?: string;
    activeLink6?: string;
}

const OrganisationSide: React.FC<OrganisationSideProps> = ({ activeLink1, activeLink2 }) => {
    return (
        <>
            <div
                className="grid gap-6 text-normal font-semibold text-muted-foreground" x-chunk="dashboard-04-chunk-0"
            >
                <Link to="/organisation" className={`${activeLink1} text-primary`}>
                    Organisation
                </Link>
                <Link to="/organisation/settings" className={`${activeLink2} text-primary`}>Settings</Link>
            </div >
        </>
    )
}

export default OrganisationSide