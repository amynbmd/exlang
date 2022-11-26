import { CommonModule } from '@angular/common';
import { ChangeDetectionStrategy, Component, OnInit } from '@angular/core';
import { Profile } from '../account/_models/profile';
import { User } from '../account/_models/user';
import { CommunityConnectionsComponent } from '../community-connections/community-connections.component';

@Component({
  selector: 'app-connections',
  templateUrl: './connections.component.html',
  styleUrls: ['./connections.component.css'],
  changeDetection: ChangeDetectionStrategy.OnPush,
  standalone: true,
  imports: [	
    CommonModule,
    CommunityConnectionsComponent
  ]
})
export class ConnectionsComponent implements OnInit {
  users: User[] = [];

  constructor() { }

  ngOnInit() {
    this.getProfiles();
  }

  getProfiles() {
    const profile1: Profile = {
      email: 'user1@email.com',
      wordofTheDay: '',
      isOnline: false,
      countryCode: 'US',
      picURL: './../../../assets/fake-people/person6.jpg',
      bio: '',
      nativeLang: 'en',
      learningLang: ['en'],
      level: '',
      interests: ['Cooking', 'Movie'],
      connected: true
    };

    const profile2: Profile = {
      email: 'user2@email.com',
      wordofTheDay: '',
      isOnline: false,
      countryCode: 'US',
      picURL: './../../../assets/fake-people/person7.jpg',
      bio: '',
      nativeLang: 'en',
      learningLang: ['en'],
      level: '',
      interests: ['Pets', 'Sports'],
      connected: true
    };

    let user1: User = {
      name: 'Jen',
      email: 'user1@email.com',
      password: '',
      profile: profile1
    };
    let user2: User = {
      name: 'Sherry',
      email: 'user2@email.com',
      password: '',
      profile: profile2
    };

    this.users.push(user1);
    this.users.push(user2);
  }
}
