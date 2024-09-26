import { Link } from "react-router-dom"

interface SettingSideProps {
    activeLink1?: string;
    activeLink2?: string;
    activeLink3?: string;
    activeLink4?: string;
    activeLink5?: string;
    activeLink6?: string;
}

const SettingSide: React.FC<SettingSideProps> = ({ activeLink1, activeLink2, activeLink3, activeLink4, activeLink5, activeLink6 }) => {
    return (
        <>
            <div
                className="grid gap-6 text-normal font-semibold text-muted-foreground" x-chunk="dashboard-04-chunk-0"
            >
                <Link to="/dashboard/settings/biodata" className={`${activeLink1} text-primary`}>
                    Biodata
                </Link>
                <Link to="/dashboard/settings/account" className={`${activeLink2} text-primary`}>Account Info</Link>
                <Link to="/dashboard/settings/contact" className={`${activeLink3} text-primary`}>Contact Info</Link>
                <Link to="#" className={`${activeLink4} text-primary`}>Security</Link>
                <Link to="#" className={`${activeLink5} text-primary`}>Payments</Link>
                <Link to="#" className={`${activeLink6} text-primary`}>Notifications</Link>
            </div >
        </>
    )
}

export default SettingSide