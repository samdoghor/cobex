import axios from "axios";
import { cobex_api } from "../utils/api-endpoints";
import { useMutation, useQuery } from '@tanstack/react-query';
import { LoginData, Member, registrationData, updateData } from "../data/type";

const memberId = localStorage.getItem('Cobex-EUI');

interface memberData {
    code: number;
    code_status: string;
    data: Member;
}

export const useMemberLoginMutation = () => {
    return useMutation({
        mutationFn: async (loginData: LoginData) => {
            const response = await axios.post(
                `${import.meta.env.VITE_API_PATH}${cobex_api.login}`,
                loginData,
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

export const useMemberLogoutMutation = () => {
    return useMutation({
        mutationFn: async () => {
            const response = await axios.post(
                `${import.meta.env.VITE_API_PATH}${cobex_api.logout}`,
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

export const useMemberRegistrationMutation = () => {
    return useMutation({
        mutationFn: async (registrationData: registrationData) => {
            const response = await axios.post(
                `${import.meta.env.VITE_API_PATH}${cobex_api.members}`,
                registrationData,
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

const getOneMember = async (): Promise<memberData> => {
    const response = await axios.get(
        `${import.meta.env.VITE_API_PATH}${cobex_api.members}/${memberId}`
    );
    return response.data
}

export const useMember = () => {
    return useQuery({
        queryKey: ["member"],
        queryFn: getOneMember,
    })
}

export const useMemberUpdateMutation = () => {
    return useMutation({
        mutationFn: async (updateData: updateData) => {
            const response = await axios.put(
                `${import.meta.env.VITE_API_PATH}${cobex_api.members}/${memberId}`,
                updateData,
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
