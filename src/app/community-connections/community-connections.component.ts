import { CommonModule } from '@angular/common';
import { ChangeDetectionStrategy, Component, Input, OnInit } from '@angular/core';
import { Observable } from 'rxjs';
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
  @Input() users: User[] = [];
  languages$: Observable<SelectItem[]>;

  constructor(private _authService: AuthenticationService) { }

  ngOnInit() {
    this.languages$ = this._authService.getLanguages();
  }
}
