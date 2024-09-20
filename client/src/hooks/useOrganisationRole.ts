import axios from "axios";
import { cobex_api } from "../utils/api-endpoints";
import { useMutation } from '@tanstack/react-query'
import { orgRegistrationRoleData } from "../data/type";



export const useOrganisationRoleRegistrationMutation = () => {
    return useMutation({
        mutationFn: async (orgRegistrationRoleData: orgRegistrationRoleData) => {
            const response = await axios.post(
                `${import.meta.env.VITE_API_PATH}${cobex_api.organisational_roles}`,
                orgRegistrationRoleData,
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

