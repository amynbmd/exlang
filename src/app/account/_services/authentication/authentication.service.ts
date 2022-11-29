import { HttpClient, HttpHeaders } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { JwtHelperService } from '@auth0/angular-jwt';
import { CookieService } from 'ngx-cookie';
import { BehaviorSubject, map, Observable } from 'rxjs';
import { AuthenticationResponse } from 'src/app/account/_models/authentication-response';
import { Login } from 'src/app/account/_models/login';
import { Registration } from 'src/app/account/_models/registration';
import { Availability } from 'src/app/user-profile-area/_models/availability';
import { SessionSetting } from 'src/app/user-profile-area/_models/session-setting';
import { Timezone } from 'src/app/user-profile-area/_models/Timezone';
import { Jwt } from 'src/app/_models/jwt';
import { SelectItem } from 'src/app/_models/select-item';
import { ConfigService } from 'src/app/_shared/config/config.service';
import { Profile } from '../../_models/profile';
import { SignUpProfile } from '../../_models/sign-up-profile';
import { User } from '../../_models/user';


@Injectable({
  providedIn: 'root'
})
export class AuthenticationService {
  private readonly baseUrl = this._configService.config?.apiUrl;
  
  private readonly httpOptions = {
    headers: new HttpHeaders({
        "Content-Type": "application/json"
    })
  };

  loggedIn = new BehaviorSubject(false);

  constructor(private _http: HttpClient, private _configService: ConfigService, private _cookieService: CookieService, private _jwtHelper: JwtHelperService) {
    if (localStorage.getItem("loggedIn") == "true") {
      let user = this.getUserFromLocalStorage();
      this.setLoggedIn(user);
    }
  }

  login(credential: Login): Observable<User> {
    let body = new FormData();
    body.append('email', credential.email);
    body.append('password', credential.password);

    return this._http.post<User>(this.baseUrl + 'login', body).pipe(
      map(res => {
        return res;
      })
    )
  }

  register(credential: Registration):Observable<User> {
    let body = new FormData();
    body.append('email', credential.email);
    body.append('name', credential.name);
    body.append('password', credential.password);
    body.append('confirmPassword', credential.confirmPassword);

    return this._http.post<User>(this.baseUrl + 'register', body).pipe(
      map(res => {
        return res;
      })
    );
  }

  updateUserProfile(profile: SignUpProfile):Observable<User> {
    return this._http.post<User>(this.baseUrl + '/user/profile', profile).pipe(
      map(res => {
        return res;
      })
    );
  }

  updateSessionSetting(sessionSetting: SessionSetting):Observable<SessionSetting> {
    return this._http.post<SessionSetting>(this.baseUrl + '/user/session-setting', sessionSetting).pipe(
      map(res => {
        return res;
      })
    );
  }

  getUserAvailability(email: string | null):Observable<Availability> {
    return this._http.get<Availability>(this.baseUrl + 'user/availability/' + email).pipe(
      map(res => {
        return res;
      })
    )
  }

  updateUserAvailability(availability: Availability) {
    return this._http.post<User>(this.baseUrl + '/user/availability', availability).pipe(
      map(res => {
        return res;
      })
    );
  }

  getUserProfile(email: string):Observable<User> {
    return this._http.get<User>(this.baseUrl + 'user/profile/' + email).pipe(
      map(res => {
        return res;
      })
    )
  }

  getUsersProfile(email: string | null):Observable<User[]> {
    return this._http.get<User[]>(this.baseUrl + 'user/' + email).pipe(
      map(res => {
        return res;
      })
    )
  }

  getConnectedUsersProfile(email: string | null):Observable<User[]> {
    return this._http.get<User[]>(this.baseUrl + 'user/connected/' + email).pipe(
      map(res => {
        res.forEach(user => {
          user.profile.connected = true;
        });

        return res;
      })
    )
  }

  getCountries():Observable<SelectItem[]> {
    return this._http.get<SelectItem[]>(this.baseUrl + 'countries').pipe(
      map(res => {
        return res;
      })
    )
  }

  getLanguages():Observable<SelectItem[]> {
    return this._http.get<SelectItem[]>(this.baseUrl + 'languages').pipe(
      map(res => {
        return res;
      })
    )
  }

  getLevels():Observable<SelectItem[]> {
    return this._http.get<SelectItem[]>(this.baseUrl + 'levels').pipe(
      map(res => {
        return res;
      })
    )
  }
  
  getTimezones():Observable<SelectItem[]> {
    return this._http.get<Timezone[]>(this.baseUrl + 'timezones').pipe(
      map(res => {
        const items: SelectItem[] = [];

        res.forEach(item => {
          items.push({name: item.text, code: item.abbr});
        });
        
        return items;
      })
    )
  }  

  getUserFromLocalStorage():User {
    let user: User = new User();
    user.email = localStorage.getItem("email");
    user.name = localStorage.getItem("name");

    return user;
  }

  setLoggedIn(user: User) {
    localStorage.setItem("loggedIn", "true");

    if (user.email != null && user.name != null){
      localStorage.setItem("email", user.email);
      localStorage.setItem("name", user.name);
    }

    this.loggedIn.next(true);
  }

  logout() {
    localStorage.removeItem("loggedIn");
    localStorage.removeItem("email");
    localStorage.removeItem("name");

    this.loggedIn.next(false);
  }


  userHasProfile(profile: Profile): boolean {
    if (profile.email == null || profile.email == undefined) {
      return false
    }

    if (
      (profile.wordofTheDay == null || profile.wordofTheDay == undefined) &&
      (profile.isOnline == null || profile.isOnline == undefined) &&
      (profile.countryCode == null || profile.countryCode == undefined) &&
      (profile.picURL == null || profile.picURL == undefined) &&
      (profile.countryCode == null || profile.countryCode == undefined) &&
      (profile.bio == null || profile.bio == undefined) &&
      (profile.nativeLang == null || profile.nativeLang == undefined) &&
      (profile.learningLang == null || profile.learningLang == undefined || profile.learningLang.length == 0) &&
      (profile.level == null || profile.level == undefined) &&
      (profile.interests == null || profile.interests == undefined || profile.interests.length == 0)
    ) {
      return false
    }

    return true;
  }
}
