import { CommonModule } from '@angular/common';
import { ChangeDetectionStrategy, Component, EventEmitter, Input, OnInit, Output } from '@angular/core';
import { MatButtonModule } from '@angular/material/button';
import { MatCardModule } from '@angular/material/card';
import { MatIconModule } from '@angular/material/icon';
import { Observable } from 'rxjs';
import { User } from 'src/app/account/_models/user';
import { AuthenticationService } from 'src/app/account/_services/authentication/authentication.service';
import { SelectItem } from 'src/app/_models/select-item';

@Component({
  selector: 'app-user-card',
  templateUrl: './user-card.component.html',
  styleUrls: ['./user-card.component.css'],

  changeDetection: ChangeDetectionStrategy.OnPush,
  standalone: true,
  imports: [
    CommonModule,
    MatCardModule,
    MatButtonModule,
    MatIconModule
  ]
})
export class UserCardComponent implements OnInit {
  @Input() user: User;
  @Input() languages$: Observable<SelectItem[]>;

  @Output() updated = new EventEmitter<number>();
  
  //Generate random image of fake people
  //https://this-person-does-not-exist.com/en

  currentUser: User;

  constructor(private _authService:AuthenticationService) { }

  ngOnInit() {
    this.currentUser = this._authService.getUserFromLocalStorage();
  }

  getSelectItemName(list: SelectItem[], code: string) {
    return list.filter(m => m.code == code)[0]?.name;
  }

  setDefaultPic() {
    this.user.profile.picURL = '../../assets/img/profile_picture_placeholder.png';
  }

  connect(email: string | null) {
    this._authService.connectUser(this.currentUser.email, email).subscribe();

    this.updated.emit(1);
  }

  disconnect(email: string | null) {
    this._authService.disconnectUser(this.currentUser.email, email).subscribe();

    this.updated.emit(0);
  }
}
