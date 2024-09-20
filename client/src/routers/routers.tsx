import Index from "../pages/Index";
import { createBrowserRouter } from 'react-router-dom';
import Learn from "../pages/Learn";
import Contact from "../pages/Contact";
import Login from "../pages/auth/Login";
import Register from "../pages/auth/Register";
import Cooperatives from "../pages/Cooperatives";
import Dashboard from "../pages/(account)/Dashboard";
import MemberRegistration from "../pages/auth/MemberRegistration";
import NotFound from "../pages/NotFound";

const routers = createBrowserRouter([
    {
        path: "/",
        element: <Index />,
    },
    {
        path: "*",
        element: <NotFound />,
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
]);

export default routers