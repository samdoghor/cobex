import axios from "axios";
import { cobex_api } from "../utils/api-endpoints";
import { useMutation, useQuery } from '@tanstack/react-query'
import { Organisation, orgRegistrationData, Member } from "../data/type";

const memberId = localStorage.getItem('Cobex-EUI');
interface organisationData {
    code: number;
    code_status: string;
    data: Organisation[];
}

interface organisationOneData {
    code: number;
    code_status: string;
    data: Organisation;
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

interface memberData {
    code: number;
    code_status: string;
    data: Member;
}

const getOneMember = async (): Promise<memberData> => {
    const response = await axios.get(
        `${import.meta.env.VITE_API_PATH}${cobex_api.members}/${memberId}`
    );
    return response.data.data.organisation
}

const getOneOrganisation = async (): Promise<organisationOneData> => {
    const organisationId = await getOneMember();
    console.log(organisationId)
    const response = await axios.get(
        `${import.meta.env.VITE_API_PATH}${cobex_api.organisations}/${organisationId}`
    );
    return response.data
}

export const useOneOrganisation = () => {
    return useQuery({
        queryKey: ["organisation"],
        queryFn: getOneOrganisation,
    })
}
