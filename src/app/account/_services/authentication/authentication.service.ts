import { HttpClient, HttpHeaders } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { JwtHelperService } from '@auth0/angular-jwt';
import { CookieService } from 'ngx-cookie';
import { BehaviorSubject, map, Observable } from 'rxjs';
import { AuthenticationResponse } from 'src/app/account/_models/authentication-response';
import { Login } from 'src/app/account/_models/login';
import { Registration } from 'src/app/account/_models/registration';
import { Jwt } from 'src/app/_models/jwt';
import { ConfigService } from 'src/app/_shared/config/config.service';


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
      this.setLoggedIn();
    }
  }

  login(credential: Login): Observable<any> {
    let body = new FormData();
    body.append('email', credential.email);
    body.append('password', credential.password);

    return this._http.post<AuthenticationResponse>(this.baseUrl + 'login', body).pipe(
      map(res => {
        return res;
      })
    )
  }

  register(credential: Registration) {
    let body = new FormData();
    body.append('email', credential.email);
    body.append('name', credential.name);
    body.append('password', credential.password);
    body.append('confirmPassword', credential.confirmPassword);

    return this._http.post<AuthenticationResponse>(this.baseUrl + 'register', body).pipe(
      map(res => {
        return res;
      })
    );
  }


  setLoggedIn() {
    localStorage.setItem("loggedIn", "true");
    this.loggedIn.next(true);
  }

  logout() {
    localStorage.removeItem("loggedIn");
    this.loggedIn.next(false);
  }
}
