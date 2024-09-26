export interface LoginData {
    email: string;
    password: string;
}

export interface registrationData {
    first_name: string;
    last_name: string;
    email: string;
    password: string;
    organisation: string | number | undefined;
    organisational_role: string | number | undefined;
}

export interface orgRegistrationData {
    full_name: string;
    email: string;
    short_name: string;
}

export interface orgRegistrationRoleData {
    role: string;
    is_top_role: boolean;
    is_member_role: boolean;
    role_position: number;
    organisation: string;
}

export interface LoginResponse {
    access_token: string;
    email: string;
    id: string
}


export interface Organisation {
    address: string | null;
    banner: string | null;
    banner_id: string | null;
    can_loan: boolean;
    city: string | null;
    country: string | null;
    created_at: string;
    date_of_establishment: string | null;
    date_of_incorporation: string | null;
    description: string | null;
    email: string;
    full_name: string;
    hq_id: string;
    id: string;
    is_hq: boolean;
    is_incorporated: boolean;
    legal_name: string | null;
    logo: string | null;
    logo_id: string | null;
    phone: string | null;
    postal_code: string | null;
    setup_completed: boolean;
    slogan: string | null;
    state: string | null;
    updated_at: string;
    short_name: string;
    verified: boolean;
    website: string | null;
}

export interface Member {
    address: string | null
    city: string | null;
    country: string | null;
    created_at: string;
    date_of_birth: string | null;
    email: string;
    employment_status: string | null;
    first_name: string;
    id: string;
    image: string | null;
    image_id: string | null;
    last_name: string;
    marital_status: string | null;
    membership_status: string;
    middle_name: string | null;
    occupation: string | null;
    organisation: string;
    organisational_role: string;
    password: string | null;
    phone: string | null;
    postal_code: string | null;
    setup_completed: boolean;
    state: string | null;
    updated_at: string | null;
    username: string;
    verified: boolean;
}

export interface updateData {
    address?: string | null
    city?: string | null;
    country?: string | null;
    date_of_birth?: string | null;
    email?: string;
    employment_status?: string | null;
    first_name?: string;
    image?: string | null;
    image_id?: string | null;
    last_name?: string;
    marital_status?: string | null;
    membership_status?: string;
    middle_name?: string | null;
    occupation?: string | null;
    organisational_role?: string;
    password?: string;
    phone?: string | null;
    postal_code?: string | null;
    setup_completed?: boolean;
    state?: string | null;
    username?: string;
    verified?: boolean;
}