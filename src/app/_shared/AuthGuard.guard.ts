import { Injectable } from '@angular/core';
import {
  CanActivate,
  ActivatedRouteSnapshot,
  RouterStateSnapshot,
  Router,
} from '@angular/router';
import { Observable, of } from 'rxjs';
import { catchError, map } from 'rxjs/operators';

import { AuthenticationService } from 'src/app/account/_services/authentication/authentication.service';
@Injectable({
  providedIn: 'root',
})
export class AuthGuard implements CanActivate {
  constructor(
    private _authService: AuthenticationService,
    private router: Router
  ) {}
  canActivate(
    next: ActivatedRouteSnapshot,
    state: RouterStateSnapshot
  ): Observable<boolean> {
    return this._authService.loggedIn.asObservable().pipe(
        map(e => {
          if (e) {
            return true;
          } else {
            this.router.navigate(['/account/area']);
            return false;
          }
        }),
        catchError((err) => {
          this.router.navigate(['']);
          return of(false);
        })
      );
  }
}
