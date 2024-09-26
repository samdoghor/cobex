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

const Profile = () => {

    const { data: memberData } = useMember();
    const { mutate, data: updateMemberData, isSuccess, isError, error } = useMemberUpdateMutation();
    const [isEditingFirstName, setIsEditingFirstName] = useState(false);
    const [isEditingLastName, setIsEditingLastName] = useState(false);
    const [isEditingMiddleName, setIsEditingMiddleName] = useState(false);
    const [isEditingDOB, setIsEditingDOB] = useState(false);
    const [showToast, setShowToast] = useState(false);
    const [errorShowToast, errorSetShowToast] = useState(false);

    const handleEditClickFirstName = () => {
        setIsEditingFirstName(true);
    };
    const handleCancelEditClickFirstName = () => {
        setIsEditingFirstName(false);
    };

    const handleEditClickLastName = () => {
        setIsEditingLastName(true);
    };
    const handleCancelEditClickLastName = () => {
        setIsEditingLastName(false);
    };

    const handleEditClickMiddleName = () => {
        setIsEditingMiddleName(true);
    };
    const handleCancelEditClickMiddleName = () => {
        setIsEditingMiddleName(false);
    };

    const handleEditClickDOB = () => {
        setIsEditingDOB(true);
    };
    const handleCancelEditClickDOB = () => {
        setIsEditingDOB(false);
    };



    const formik = useFormik({
        initialValues: {
            date_of_birth: memberData?.data.date_of_birth || "",
            first_name: memberData?.data.first_name || "",
            // image: memberData?.data.image || "",
            // image_id: memberData?.data.image_id || "",
            last_name: memberData?.data.last_name || "",
            middle_name: memberData?.data.middle_name || "",
        },
        validationSchema: Yup.object({
            date_of_birth: Yup.string(),
            first_name: Yup.string(),
            // image: Yup.string(),
            // image_id: Yup.string(),
            last_name: Yup.string(),
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
            setIsEditingFirstName(false);
            setIsEditingLastName(false);
            setIsEditingMiddleName(false);
            setIsEditingDOB(false);
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
                    <SettingTitle page="biodata" />
                    <div className="mx-auto grid w-full max-w-6xl items-start gap-6 md:grid-cols-[180px_1fr] lg:grid-cols-[250px_1fr]">
                        <SettingSide
                            activeLink1="font-semibold"
                            activeLink2="font-normal"
                            activeLink3="font-normal"
                            activeLink4="font-normal"
                            activeLink5="font-normal"
                            activeLink6="font-normal"
                        />
                        <div className="grid gap-6">

                            <Card x-chunk="dashboard-04-chunk-1" className="bg-gradient-to-r from-slate-400 to-gray-400">
                                <CardHeader>
                                    <CardTitle>First Name</CardTitle>
                                </CardHeader>
                                {isEditingFirstName ? (
                                    <form onSubmit={formik.handleSubmit}>
                                        <CardContent>
                                            <Input type="text" value={formik.values.first_name} onChange={formik.handleChange} name="first_name" id="first_name" />
                                        </CardContent>
                                        <CardFooter className="border-t px-6 py-4 border-slate-500 gap-4">
                                            <button className="bg-primary text-primary-foreground hover:bg-primary/90 h-10 px-4 py-2 rounded-md font-semibold" type="submit">Save</button>
                                            <Button onClick={handleCancelEditClickFirstName}>Cancel</Button>
                                        </CardFooter>
                                    </form>
                                ) : (
                                    <>
                                        <CardContent>
                                            <Input value={memberData?.data.first_name || ''} disabled />
                                        </CardContent>
                                        <CardFooter className="border-t px-6 py-4 border-slate-500">
                                            <Button onClick={handleEditClickFirstName}>Edit</Button>
                                        </CardFooter>
                                    </>
                                )
                                }
                            </Card>
                            <Card x-chunk="dashboard-04-chunk-1" className="bg-gradient-to-r from-slate-400 to-gray-400">
                                <CardHeader>
                                    <CardTitle>Last Name</CardTitle>
                                </CardHeader>
                                {isEditingLastName ? (
                                    <form onSubmit={formik.handleSubmit}>
                                        <CardContent>
                                            <Input type="text" value={formik.values.last_name} onChange={formik.handleChange} name="last_name" id="last_name" />
                                        </CardContent>
                                        <CardFooter className="border-t px-6 py-4 border-slate-500 gap-4">
                                            <button className="bg-primary text-primary-foreground hover:bg-primary/90 h-10 px-4 py-2 rounded-md font-semibold" type="submit">Save</button>
                                            <Button onClick={handleCancelEditClickLastName}>Cancel</Button>
                                        </CardFooter>
                                    </form>
                                ) : (
                                    <>
                                        <CardContent>
                                            <Input value={memberData?.data.last_name || ''} disabled />
                                        </CardContent>
                                        <CardFooter className="border-t px-6 py-4 border-slate-500">
                                            <Button onClick={handleEditClickLastName}>Edit</Button>
                                        </CardFooter>
                                    </>
                                )
                                }
                            </Card>
                            <Card x-chunk="dashboard-04-chunk-1" className="bg-gradient-to-r from-slate-400 to-gray-400">
                                <CardHeader>
                                    <CardTitle>Middle Name</CardTitle>
                                </CardHeader>
                                {isEditingMiddleName ? (
                                    <form onSubmit={formik.handleSubmit}>
                                        <CardContent>
                                            <Input type="text" value={formik.values.middle_name} onChange={formik.handleChange} name="middle_name" id="middle_name" />
                                        </CardContent>
                                        <CardFooter className="border-t px-6 py-4 border-slate-500 gap-4">
                                            <button className="bg-primary text-primary-foreground hover:bg-primary/90 h-10 px-4 py-2 rounded-md font-semibold" type="submit">Save</button>
                                            <Button onClick={handleCancelEditClickMiddleName}>Cancel</Button>
                                        </CardFooter>
                                    </form>
                                ) : (
                                    <>
                                        <CardContent>
                                            <Input value={memberData?.data.middle_name || ''} disabled />
                                        </CardContent>
                                        <CardFooter className="border-t px-6 py-4 border-slate-500">
                                            <Button onClick={handleEditClickMiddleName}>Edit</Button>
                                        </CardFooter>
                                    </>
                                )
                                }
                            </Card>

                            <Card x-chunk="dashboard-04-chunk-1" className="bg-gradient-to-r from-slate-400 to-gray-400">
                                <CardHeader>
                                    <CardTitle>Date of Birth</CardTitle>
                                </CardHeader>
                                {isEditingDOB ? (
                                    <form onSubmit={formik.handleSubmit}>
                                        <CardContent>
                                            <Input type="date" value={formik.values.date_of_birth} onChange={formik.handleChange} name="date_of_birth" id="date_of_birth" />
                                        </CardContent>
                                        <CardFooter className="border-t px-6 py-4 border-slate-500 gap-4">
                                            <button className="bg-primary text-primary-foreground hover:bg-primary/90 h-10 px-4 py-2 rounded-md font-semibold" type="submit">Save</button>
                                            <Button onClick={handleCancelEditClickDOB}>Cancel</Button>
                                        </CardFooter>
                                    </form>
                                ) : (
                                    <>
                                        <CardContent>
                                            <Input value={memberData?.data.date_of_birth || ''} disabled />
                                        </CardContent>
                                        <CardFooter className="border-t px-6 py-4 border-slate-500">
                                            <Button onClick={handleEditClickDOB}>Edit</Button>
                                        </CardFooter>
                                    </>
                                )
                                }
                            </Card>
                        </div>
                    </div>
                </main>
            </div>
            {showToast && (
                <Toaster
                    codeStatus={updateMemberData?.code_status}
                    onDismiss={() => setShowToast(false)}
                    bgColor="bg-green-950"
                    toastIcon={<HiBadgeCheck className="h-5 w-5 bg-green-700 rounded-lg" />}
                />
            )}
            {errorShowToast && (
                <Toaster
                    //@ts-expect-error - datatype error
                    codeStatus={error?.response?.data?.code_message}
                    onDismiss={() => errorSetShowToast(false)}
                    bgColor="bg-red-950"
                    toastIcon={<HiXCircle className="h-5 w-5 bg-red-700 rounded-lg" />}
                />
            )}
            <Footer />
        </>
    )
}

export default Profile