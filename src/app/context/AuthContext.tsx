"use client";

import { createContext, useState, useEffect, ReactNode } from "react";
import Cookies from "js-cookie";
import { getUser, logout } from "@/app/utils/api";

// Define the Auth Context Type
interface AuthContextType {
    user: string | null;
    setUser: (user: string | null) => void;
    handleLogout: () => void;
}

// Create Auth Context
export const AuthContext = createContext<AuthContextType>({
    user: null,
    setUser: () => {},
    handleLogout: () => {},
});

// Auth Provider Component
export const AuthProvider = ({ children }: { children: ReactNode }) => {
    const [user, setUser] = useState<string | null>(null);

    useEffect(() => {
        const fetchUser = async () => {
            const userData = await getUser();
            if (userData) {
                setUser(userData.username);
            }
        };
        fetchUser();
    }, []);

    const handleLogout = () => {
        logout();
        setUser(null);
    };

    return (
        <AuthContext.Provider value={{ user, setUser, handleLogout }}>
            {children}
        </AuthContext.Provider>
    );
};