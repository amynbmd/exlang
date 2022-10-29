import { HttpClient, HttpHeaders } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { JwtHelperService } from '@auth0/angular-jwt';
import { CookieService } from 'ngx-cookie';
import { BehaviorSubject, map, Observable } from 'rxjs';
import { AuthenticationResponse } from 'src/app/account/_models/authentication-response';
import { Login } from 'src/app/account/_models/login';
import { Registration } from 'src/app/account/_models/registration';
import { Jwt } from 'src/app/_models/jwt';
import { SelectItem } from 'src/app/_models/select-item';
import { ConfigService } from 'src/app/_shared/config/config.service';
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

  getUserProfile(email: string):Observable<User> {
    return this._http.get<User>(this.baseUrl + 'user/profile/' + email).pipe(
      map(res => {
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
}
