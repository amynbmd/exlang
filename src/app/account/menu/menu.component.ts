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
    this._router.navigate(['account', 'info', 1]);
  }

  login() {
    this._router.navigate(['account', 'login']);
  }

  logout() {
    this._router.navigate(['account', 'logout', 1]);
  }
}