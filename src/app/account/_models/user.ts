import { Profile } from "./profile";

export class User {
    name: string | null;
    email: string | null;
    password: string;
    profile: Profile;
}
