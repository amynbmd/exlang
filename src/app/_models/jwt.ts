export interface Jwt {
    id: string;
    email: string;
    exp: Date;
    iat: Date;
    jti: string;
    nbf: Date;
    sub: string;
}
