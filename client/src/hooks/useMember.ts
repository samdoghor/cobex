import axios from "axios";
import { cobex_api } from "../utils/api-endpoints";
import { useMutation } from '@tanstack/react-query';
import { LoginData, registrationData } from "../data/type";

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

