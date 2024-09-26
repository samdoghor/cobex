import Index from "../pages/Index";
import { createBrowserRouter } from 'react-router-dom';
import Learn from "../pages/Learn";
import Contact from "../pages/Contact";
import Login from "../pages/auth/Login";
import Register from "../pages/auth/Register";
import Cooperatives from "../pages/Cooperatives";
import Dashboard from "../pages/account/Dashboard";
import MemberRegistration from "../pages/auth/MemberRegistration";
import NotFound from "../pages/NotFound";
import Profile from "@/pages/account/Profile";
import Account from "@/pages/account/Account";
import ContactInfo from "@/pages/account/ContactInfo";
import Organisation from "@/pages/account/Organisation";
import OrganisationSetting from "@/pages/account/OrganisationSetting";

const routers = createBrowserRouter([
    {
        path: "/",
        element: <Index />,
    },
    {
        path: "/cooperatives",
        element: <Cooperatives />,
    },
    {
        path: "/learn",
        element: <Learn />,
    },
    {
        path: "/contact",
        element: <Contact />,
    },
    {
        path: "/auth/login",
        element: <Login />,
    },
    {
        path: "/auth/register",
        element: <Register />,
    },
    {
        path: "/auth/register/member",
        element: <MemberRegistration />,
    },
    {
        path: "/dashboard",
        element: <Dashboard />,
    },
    {
        path: "/dashboard/settings/biodata",
        element: <Profile />,
    },
    {
        path: "/dashboard/settings/account",
        element: <Account />,
    },
    {
        path: "/dashboard/settings/contact",
        element: <ContactInfo />,
    },
    {
        path: "/organisation",
        element: <Organisation />,
    },
    {
        path: "/organisation/settings",
        element: <OrganisationSetting />,
    },
    {
        path: "*",
        element: <NotFound />,
    },
]);

export default routers