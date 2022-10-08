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
  private readonly baseUrl = this._configService.config?.apiUrl + 'authentication/';
  
  private readonly httpOptions = {
    headers: new HttpHeaders({
        "Content-Type": "application/json"
    })
  };

  loggedIn = new BehaviorSubject(false);

  constructor(private _http: HttpClient, private _configService: ConfigService, private _cookieService: CookieService, private _jwtHelper: JwtHelperService) { 
    this.isLoggedInAndValid();
  }

  login(credential: Login): Observable<any> {
    return this._http.post<AuthenticationResponse>(this.baseUrl + 'login', credential, this.httpOptions).pipe(
      map(res => {
        if (res.success) {
          this.storeJwt(res);
          this.isLoggedInAndValid();
        }
        return res;
      })
    )
  }

  register(credential: Registration) {
    return this._http.post<AuthenticationResponse>(this.baseUrl + 'register', credential, this.httpOptions).pipe(
      map(res => {
        return res;
      })
    );
  }
  private isLoggedInAndValid() {
    let jwt = this.getJwt();

    if (jwt == null || jwt == undefined) {
      return this.loggedIn.next(false);
    }

    if (this._jwtHelper.isTokenExpired(this._cookieService.get('jwt'))) {
      return this.loggedIn.next(false);
    }

    return this.loggedIn.next(true);
  }

  private getJwt(): Jwt {
    return this._jwtHelper.decodeToken(this._cookieService.get('jwt'));
  }

  private storeJwt(authRes: AuthenticationResponse) {
    this._cookieService.put("jwt", authRes.token);
  }
}
