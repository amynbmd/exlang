import { ChangeDetectionStrategy, Component, OnInit } from '@angular/core';
import { AppointmentAreaComponent } from './appointment-area/appointment-area.component';
import { UserBioComponent } from './user-bio/user-bio.component';
import { MatDividerModule } from '@angular/material/divider';
import { FormModule } from '../_modules/form.module';
import { MatIconModule } from '@angular/material/icon';

@Component({
  selector: 'app-user-profile-area',
  templateUrl: './user-profile-area.component.html',
  styleUrls: ['./user-profile-area.component.scss'],
  changeDetection: ChangeDetectionStrategy.OnPush,
  standalone: true,
  imports: [
    UserBioComponent,
    AppointmentAreaComponent,
    MatDividerModule,
    MatIconModule
  ]
})
export class UserProfileAreaComponent implements OnInit {
  pic: string = '';

  constructor() { }

  ngOnInit() {
    this.pic = '../../assets/img/my-bear.jpg';
  }


  setDefaultPic() {
    this.pic = '../../assets/img/profile_picture_placeholder.png';
  }
}
