
export class Availability {
    email: string | null;
    sunday: Time;
    monday: Time;
    tuesday: Time;
    wednesday: Time;
    thursday: Time;
    friday: Time;
    saturday: Time;
}


export class Time {
    isAvailable: boolean;
    startTime: string | null;
    endTime: string | null;
}