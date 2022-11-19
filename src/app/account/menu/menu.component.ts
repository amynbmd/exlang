import { Component, OnInit } from '@angular/core';
import { Router } from '@angular/router';
import { Observable } from 'rxjs';
import { AuthenticationService } from 'src/app/account/_services/authentication/authentication.service';

@Component({
  selector: 'account-menu',
  templateUrl: './menu.component.html',
  styleUrls: ['./menu.component.scss', '../_shared/styles.scss']
})
export class MenuComponent implements OnInit {
  loggedIn = this._authService.loggedIn;

  constructor(private _router: Router, private _authService: AuthenticationService) { }

  ngOnInit() {
  }

  goToAccountInfo() {
    this._router.navigate(['user-profile-area']);
  }

  login() {
    this._router.navigate(['account', 'area'])
    .then(() => {
      window.location.reload();
    });
  }

  logout() {
    this._authService.logout();
    this._router.navigate(['account', 'area'])
    .then(() => {
      window.location.reload();
    });
  }
}
