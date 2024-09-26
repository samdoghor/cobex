import Footer from "@/components/Footer"
import InnerHeader from "@/components/InnerHeader"

import { Button } from "@/components/ui/button"
import {
    Card,
    CardContent,
    CardFooter,
    CardHeader,
    CardTitle,
} from "@/components/ui/card"
import { Input } from "@/components/ui/input"
import SettingSide from "@/components/SettingSide"
import SettingTitle from "@/components/SettingTitle"
import { useMember, useMemberUpdateMutation } from "@/hooks/useMember"
import { useEffect, useState } from "react"
import * as Yup from 'yup';
import { useFormik } from 'formik';
import Toaster from "../../components/Toaster";
import { HiBadgeCheck, HiXCircle } from "react-icons/hi";

const Account = () => {

    const { data: memberData } = useMember();
    const { mutate, data: updateMemberData, isSuccess, isError, error } = useMemberUpdateMutation();
    const [isEditingEmail, setIsEditingEmail] = useState(false);
    const [isEditingPassword, setIsEditingPassword] = useState(false);
    const [isEditingUsername, setIsEditingUsername] = useState(false);
    const [showToast, setShowToast] = useState(false);
    const [errorShowToast, errorSetShowToast] = useState(false);

    const handleEditClickEmail = () => {
        setIsEditingEmail(true);
    };
    const handleCancelEditClickEmail = () => {
        setIsEditingEmail(false);
    };

    const handleEditClickPassword = () => {
        setIsEditingPassword(true);
    };
    const handleCancelEditClickPassowrd = () => {
        setIsEditingPassword(false);
    };

    const handleEditClickUsername = () => {
        setIsEditingUsername(true);
    };
    const handleCancelEditClickUsername = () => {
        setIsEditingUsername(false);
    };

    const formik = useFormik({
        initialValues: {
            email: memberData?.data.email || "",
            password: "password",
            username: memberData?.data.username || "",
            middle_name: memberData?.data.middle_name || "",
        },
        validationSchema: Yup.object({
            email: Yup.string(),
            password: Yup.string(),
            username: Yup.string(),
            middle_name: Yup.string(),

        }),
        onSubmit: values => {
            mutate(values);
        },
    });

    useEffect(() => {
        if (isSuccess) {
            setShowToast(true);
            setTimeout(() => {
                setShowToast(false);
            }, 3000);
            setIsEditingEmail(false);
            setIsEditingPassword(false);
            setIsEditingUsername(false);
            window.location.reload();
        }

        if (isError) {
            errorSetShowToast(true);
            setTimeout(() => {
                errorSetShowToast(false);
            }, 3000);
        }
    }, [isSuccess, isError, updateMemberData, error]);

    return (
        <>
            <InnerHeader />
            <div className="flex min-h-screen w-full flex-col bg-gradient-to-b from-slate-200 to-slate-300">
                <main className="flex min-h-[calc(100vh_-_theme(spacing.16))] flex-1 flex-col gap-4 bg-muted/40 p-4 md:gap-8 md:p-10">
                    <SettingTitle page="account-info" />
                    <div className="mx-auto grid w-full max-w-6xl items-start gap-6 md:grid-cols-[180px_1fr] lg:grid-cols-[250px_1fr]">
                        <SettingSide
                            activeLink1="font-normal"
                            activeLink2="font-semibold"
                            activeLink3="font-normal"
                            activeLink4="font-normal"
                            activeLink5="font-normal"
                            activeLink6="font-normal"
                        />
                        <div className="grid gap-6">
                            <Card x-chunk="dashboard-04-chunk-1" className="bg-gradient-to-r from-slate-400 to-gray-400">
                                <CardHeader>
                                    <CardTitle>Email Address</CardTitle>
                                </CardHeader>
                                {isEditingEmail ? (
                                    <form onSubmit={formik.handleSubmit}>
                                        <CardContent>
                                            <Input type="eamil" value={formik.values.email} onChange={formik.handleChange} name="email" id="email" />
                                        </CardContent>
                                        <CardFooter className="border-t px-6 py-4 border-slate-500 gap-4">
                                            <button className="bg-primary text-primary-foreground hover:bg-primary/90 h-10 px-4 py-2 rounded-md font-semibold" type="submit">Save</button>
                                            <Button onClick={handleCancelEditClickEmail}>Cancel</Button>
                                        </CardFooter>
                                    </form>
                                ) : (
                                    <>
                                        <CardContent>
                                            <Input value={memberData?.data.email || ''} disabled />
                                        </CardContent>
                                        <CardFooter className="border-t px-6 py-4 border-slate-500">
                                            <Button onClick={handleEditClickEmail}>Edit</Button>
                                        </CardFooter>
                                    </>
                                )
                                }
                            </Card>

                            <Card x-chunk="dashboard-04-chunk-1" className="bg-gradient-to-r from-slate-400 to-gray-400">
                                <CardHeader>
                                    <CardTitle>Password</CardTitle>
                                </CardHeader>
                                {isEditingPassword ? (
                                    <form onSubmit={formik.handleSubmit}>
                                        <CardContent>
                                            <Input type="[password]" value={formik.values.password} onChange={formik.handleChange} name="password" id="password" />
                                        </CardContent>
                                        <CardFooter className="border-t px-6 py-4 border-slate-500 gap-4">
                                            <button className="bg-primary text-primary-foreground hover:bg-primary/90 h-10 px-4 py-2 rounded-md font-semibold" type="submit">Save</button>
                                            <Button onClick={handleCancelEditClickPassowrd}>Cancel</Button>
                                        </CardFooter>
                                    </form>
                                ) : (
                                    <>
                                        <CardContent>
                                            <Input value="password" disabled />
                                        </CardContent>
                                        <CardFooter className="border-t px-6 py-4 border-slate-500">
                                            <Button onClick={handleEditClickPassword}>Edit</Button>
                                        </CardFooter>
                                    </>
                                )
                                }
                            </Card>
                            <Card x-chunk="dashboard-04-chunk-1" className="bg-gradient-to-r from-slate-400 to-gray-400">
                                <CardHeader>
                                    <CardTitle>Username</CardTitle>
                                </CardHeader>
                                {isEditingUsername ? (
                                    <form onSubmit={formik.handleSubmit}>
                                        <CardContent>
                                            <Input type="text" value={formik.values.username} onChange={formik.handleChange} name="username" id="username" />
                                        </CardContent>
                                        <CardFooter className="border-t px-6 py-4 border-slate-500 gap-4">
                                            <button className="bg-primary text-primary-foreground hover:bg-primary/90 h-10 px-4 py-2 rounded-md font-semibold" type="submit">Save</button>
                                            <Button onClick={handleCancelEditClickUsername}>Cancel</Button>
                                        </CardFooter>
                                    </form>
                                ) : (
                                    <>
                                        <CardContent>
                                            <Input value={memberData?.data.username || ''} disabled />
                                        </CardContent>
                                        <CardFooter className="border-t px-6 py-4 border-slate-500">
                                            <Button onClick={handleEditClickUsername}>Edit</Button>
                                        </CardFooter>
                                    </>
                                )
                                }
                            </Card>
                        </div>
                    </div>
                </main >
            </div >
            {showToast && (
                <Toaster
                    codeStatus={updateMemberData?.code_status}
                    onDismiss={() => setShowToast(false)}
                    bgColor="bg-green-950"
                    toastIcon={<HiBadgeCheck className="h-5 w-5 bg-green-700 rounded-lg" />}
                />
            )}
            {
                errorShowToast && (
                    <Toaster
                        //@ts-expect-error - datatype error
                        codeStatus={error?.response?.data?.code_message}
                        onDismiss={() => errorSetShowToast(false)}
                        bgColor="bg-red-950"
                        toastIcon={<HiXCircle className="h-5 w-5 bg-red-700 rounded-lg" />}
                    />
                )
            }
            <Footer />
        </>
    )
}

export default Account