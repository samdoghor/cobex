import { Toast } from "flowbite-react";

interface ToastProps {
    codeStatus: string | number;
    onDismiss: () => void;
    bgColor: unknown;
    toastIcon: JSX.Element;
}


const Toaster: React.FC<ToastProps> = ({ codeStatus, onDismiss, bgColor, toastIcon }) => {
    return (
        <>
            <Toast className={`fixed top-5 right-5 ${bgColor} text-white flex items-center justify-between w-full max-w-xs`}>
                <div className="inline-flex h-8 w-8 shrink-0 items-center justify-center rounded-2xl text-white pe-2">
                    {toastIcon}
                </div>
                <div className="text-sm flex-1 font-semibold">
                    {codeStatus}
                </div>
                <Toast.Toggle onDismiss={onDismiss} className={`${bgColor}flex justify-center items-center text-white`} />
            </Toast>
        </>
    )
}

export default Toaster
