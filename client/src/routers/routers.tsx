import Index from "../pages/Index";
import { createBrowserRouter } from 'react-router-dom';
import Learn from "../pages/Learn";
import Contact from "../pages/Contact";
import Login from "../pages/auth/Login";
import Register from "../pages/auth/Register";
import Cooperatives from "../pages/Cooperatives";

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
]);

export default routers