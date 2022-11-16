import { ChangeDetectionStrategy, Component, Input, OnInit } from '@angular/core';
import { MatButtonModule } from '@angular/material/button';
import { MatCardModule } from '@angular/material/card';
import { User } from 'src/app/account/_models/user';

@Component({
  selector: 'app-user-card',
  templateUrl: './user-card.component.html',
  styleUrls: ['./user-card.component.css'],

  changeDetection: ChangeDetectionStrategy.OnPush,
  standalone: true,
  imports: [
    MatCardModule,
    MatButtonModule
  ]
})
export class UserCardComponent implements OnInit {
  @Input() user: User;
  
  //Generate random image of fake people
  //https://this-person-does-not-exist.com/en

  constructor() { }

  ngOnInit() {
  }

}
