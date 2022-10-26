import { ChangeDetectionStrategy, Component, OnInit } from '@angular/core';
import { UserBioComponent } from './user-bio/user-bio.component';

@Component({
  selector: 'app-user-profile-area',
  templateUrl: './user-profile-area.component.html',
  styleUrls: ['./user-profile-area.component.scss'],
  changeDetection: ChangeDetectionStrategy.OnPush,
  standalone: true,
  imports: [	
    UserBioComponent
  ]
})
export class UserProfileAreaComponent implements OnInit {

  constructor() { }

  ngOnInit() {
  }

}
