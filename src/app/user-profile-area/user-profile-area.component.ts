import { ChangeDetectionStrategy, Component, OnInit } from '@angular/core';
import { AppointmentAreaComponent } from './appointment-area/appointment-area.component';
import { UserBioComponent } from './user-bio/user-bio.component';
import { MatDividerModule } from '@angular/material/divider';
import { FormModule } from '../_modules/form.module';
import { MatIconModule } from '@angular/material/icon';
import { Observable } from 'rxjs';
import { User } from '../account/_models/user';
import { AuthenticationService } from '../account/_services/authentication/authentication.service';
import { CommonModule } from '@angular/common';

@Component({
  selector: 'app-user-profile-area',
  templateUrl: './user-profile-area.component.html',
  styleUrls: ['./user-profile-area.component.scss'],
  changeDetection: ChangeDetectionStrategy.OnPush,
  standalone: true,
  imports: [
    CommonModule,
    UserBioComponent,
    AppointmentAreaComponent,
    MatDividerModule,
    MatIconModule
  ]
})
export class UserProfileAreaComponent implements OnInit {
  pic: string = '';
  user$: Observable<User>;

  constructor(private _authService: AuthenticationService) { }

  ngOnInit() {
    let user = this._authService.getUserFromLocalStorage();
    if (user.email != null) {
      this.user$ = this._authService.getUserProfile(user.email);
    }
  }


  setDefaultPic() {
    this.pic = '../../assets/img/profile_picture_placeholder.png';


  }
}
