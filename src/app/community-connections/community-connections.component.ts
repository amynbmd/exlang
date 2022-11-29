import { CommonModule } from '@angular/common';
import { ChangeDetectionStrategy, ChangeDetectorRef, Component, Input, OnInit } from '@angular/core';
import { Observable, of } from 'rxjs';
import { User } from '../account/_models/user';
import { AuthenticationService } from '../account/_services/authentication/authentication.service';
import { UserCardComponent } from './user-card/user-card.component';
import { SelectItem } from '../_models/select-item';

@Component({
  selector: 'app-community-connections',
  templateUrl: './community-connections.component.html',
  styleUrls: ['./community-connections.component.css'],
  changeDetection: ChangeDetectionStrategy.OnPush,
  standalone: true,
  imports: [	
    CommonModule,
    UserCardComponent
  ]
})
export class CommunityConnectionsComponent implements OnInit {
  @Input() users$: Observable<User[]>;
  languages$: Observable<SelectItem[]>;

  constructor(private _authService: AuthenticationService, private _cd: ChangeDetectorRef ) { }

  ngOnInit() {
    this.languages$ = this._authService.getLanguages();
  }


  updateList(e: number) {
    if (e === 1) {
      // this.users$ = of([]);
      this.users$ = this._authService.getUsersProfile(this._authService.getUserFromLocalStorage().email);

    } else {
      // this.users$ = of([]);
      this.users$ = this._authService.getConnectedUsersProfile(this._authService.getUserFromLocalStorage().email);
    }

    // this._cd.markForCheck();
  }
}
