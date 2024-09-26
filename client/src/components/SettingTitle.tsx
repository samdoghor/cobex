import * as React from 'react';
interface PageTitle {
    page: string;
}

const SettingTitle: React.FC<PageTitle> = ({ page }) => {
    return (
        <>
            <div className="mx-auto grid w-full max-w-6xl gap-2">
                <h1 className="text-3xl font-semibold">settings/{page}</h1>
            </div>
        </>
    )
}

export default SettingTitle