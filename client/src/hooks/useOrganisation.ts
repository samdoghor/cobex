import axios from "axios";
import { cobex_api } from "../utils/api-endpoints";
import { useMutation, useQuery } from '@tanstack/react-query'
import { Organisation } from "../data/type";
import { orgRegistrationData } from "../data/type";


interface organisationData {
    code: number;
    code_status: string;
    data: Organisation[];
}

export const useOrganisationRegistrationMutation = () => {
    return useMutation({
        mutationFn: async (orgRegistrationData: orgRegistrationData) => {
            const response = await axios.post(
                `${import.meta.env.VITE_API_PATH}${cobex_api.organisations}`,
                orgRegistrationData,
                {
                    headers: {
                        'Content-Type': 'application/json'
                    }
                }
            );
            return response.data;
        }
    });
}

const getAllOrganisation = async (): Promise<organisationData> => {
    const response = await axios.get(
        `${import.meta.env.VITE_API_PATH}${cobex_api.organisations}`
    );
    return response.data
}

export const useOrganisation = () => {
    return useQuery({
        queryKey: ["organisation"],
        queryFn: getAllOrganisation,
    })
}
