import { ChangeDetectionStrategy, Component, OnInit } from '@angular/core';
import { AuthenticationService } from 'src/app/account/_services/authentication/authentication.service';

@Component({
  selector: 'app-sidebar',
  templateUrl: './sidebar.component.html',
  styleUrls: ['./sidebar.component.scss'],
  changeDetection: ChangeDetectionStrategy.OnPush
})
export class SidebarComponent implements OnInit {
  loggedIn = this._authService.loggedIn;
  
  constructor(private _authService: AuthenticationService) {}

  ngOnInit() {}
}
