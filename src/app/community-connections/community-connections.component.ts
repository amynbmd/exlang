import { CommonModule } from '@angular/common';
import { ChangeDetectionStrategy, ChangeDetectorRef, Component, EventEmitter, Input, OnInit, Output } from '@angular/core';
import { map, Observable, of } from 'rxjs';
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
  @Input() users: User[];
  
  languages$: Observable<SelectItem[]>;
  currentUser: User;


  constructor(private _authService: AuthenticationService, private _cd: ChangeDetectorRef ) { }

  ngOnInit() {
    this.languages$ = this._authService.getLanguages();
    this.currentUser = this._authService.getUserFromLocalStorage();
  }

  emitConnection(connectType: ConnectType) {
    if (connectType.type === 1) {
      this._authService.connectUser(this.currentUser.email, connectType.email).subscribe(response => {
        this._authService.getUsersProfile(this._authService.getUserFromLocalStorage().email).subscribe(res => {
          this.users = [...res];
          this._cd.markForCheck();
        });
      });

    } else {
      this._authService.disconnectUser(this.currentUser.email, connectType.email).subscribe(response => {
        this._authService.getConnectedUsersProfile(this._authService.getUserFromLocalStorage().email).subscribe(res => {
          this.users = [...res];
          this._cd.markForCheck();
        });
      });
    }
  }
}


export class ConnectType {
  type =  0 || 1;
  email: string
}
