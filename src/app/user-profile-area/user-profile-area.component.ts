import { ChangeDetectionStrategy, Component, OnInit } from '@angular/core';
import { AppointmentAreaComponent } from './appointment-area/appointment-area.component';
import { UserBioComponent } from './user-bio/user-bio.component';
import { MatDividerModule } from '@angular/material/divider';

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
  ]
})
export class UserProfileAreaComponent implements OnInit {

  constructor() { }

  ngOnInit() {
  }

}
